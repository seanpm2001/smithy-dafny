/*
 * Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
 *
 * Licensed under the Apache License, Version 2.0 (the "License").
 * You may not use this file except in compliance with the License.
 * A copy of the License is located at
 *
 *   http://aws.amazon.com/apache2.0
 *
 * or in the "license" file accompanying this file. This file is distributed
 * on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either
 * express or implied. See the License for the specific language governing
 * permissions and limitations under the License.
 */

package software.amazon.polymorph.smithypython;

import java.util.Collections;
import java.util.HashSet;
import java.util.List;
import java.util.Locale;
import java.util.Set;
import java.util.TreeSet;
import software.amazon.polymorph.traits.LocalServiceTrait;
import software.amazon.smithy.codegen.core.Symbol;
import software.amazon.smithy.codegen.core.SymbolReference;
import software.amazon.smithy.model.shapes.OperationShape;
import software.amazon.smithy.model.shapes.ServiceShape;
import software.amazon.smithy.model.shapes.Shape;
import software.amazon.smithy.model.shapes.ShapeId;
import software.amazon.smithy.python.codegen.ApplicationProtocol;
import software.amazon.smithy.python.codegen.ConfigField;
import software.amazon.smithy.python.codegen.GenerationContext;
import software.amazon.smithy.python.codegen.PythonWriter;
import software.amazon.smithy.python.codegen.integration.ProtocolGenerator;
import software.amazon.smithy.python.codegen.integration.RuntimeClientPlugin;
import software.amazon.smithy.python.codegen.integration.PythonIntegration;
import software.amazon.smithy.utils.CodeInterceptor;
import software.amazon.smithy.utils.CodeSection;

// TODO: Naming of DafnyIntegration?
public final class DafnyIntegration implements PythonIntegration {
    private RuntimeClientPlugin dafnyImplRuntimeClientPlugin = RuntimeClientPlugin.builder()
        .configFields(
            // Adds a new field in the client class' config.
            // This is an interface for the Dafny implementation code.
            // The Smithy-Dafny Python plugin generates a dafnyImplInterface file
            // and populates it with the relevant information from the model
            // to interact with the Dafny implementation.
            // We use an interface as we cannot plug the model into the RuntimeClientPlugin definition,
            // but we can point the RuntimeClientPlugin to an interface and plug the model in there.
            // TODO: Naming of DafnyImplInterface?
            Collections.singletonList(new ConfigField("dafnyImplInterface",
                Symbol.builder()
                    .name("DafnyImplInterface")
                    .namespace(".dafnyImplInterface", ".")
                .build(),
                // isOptional is marked as true here, but in practice, this is required.
                // The plugin will add a value immediately after Config is created.
                true, ""))
         ).pythonPlugin(
             SymbolReference.builder()
             .symbol(
                 Symbol.builder()
                 .name("set_config_impl")
                 .namespace(".plugin", ".")
                 .build())
             .build()
         )
        .build();

    @Override
    public List<? extends CodeInterceptor<? extends CodeSection, PythonWriter>>
    interceptors(GenerationContext codegenContext) {
        return List.of(new SendRequestInterceptor());
    }

    // TODO: Refactor into nameresovler
    public String clientForService(ServiceShape serviceShape) {
        if (serviceShape.hasTrait(LocalServiceTrait.class)) {
            return serviceShape.expectTrait(LocalServiceTrait.class).getSdkId() + "Client";
        } else {
            throw new UnsupportedOperationException("Non-local services not supported");
        }
    }
    public String shimForService(ServiceShape serviceShape) {
        if (serviceShape.hasTrait(LocalServiceTrait.class)) {
            return serviceShape.expectTrait(LocalServiceTrait.class).getSdkId() + "Shim";
        } else {
            throw new UnsupportedOperationException("Non-local services not supported");
        }
    }

    @Override
    public void customize(GenerationContext codegenContext) {
        // TODO: Refactor into a nameResolver and call nameForService
        // TODO: Support more than 1 service (will throw IndexOutOfBoundsException if >1 service)
        ServiceShape serviceShape = (ServiceShape) codegenContext.model().getServiceShapes().toArray()[0];
        String clientName = clientForService(serviceShape);

        // TODO: nameResolver
        String moduleName =  codegenContext.settings().getModuleName();
        String implModulePrelude = serviceShape.getId().getNamespace().toLowerCase(Locale.ROOT) + ".internaldafny.impl";

        // TODO: refactor to PluginFileWriter; do imports, etc. correctly
        // TODO: Naming of this file?
        codegenContext.writerDelegator().useFileWriter(moduleName + "/plugin.py", "", writer -> {
            writer.write(
            """
            from .config import Config, Plugin
            from smithy_python.interfaces.retries import RetryStrategy
            from smithy_python.exceptions import SmithyRetryException
            from .dafnyImplInterface import DafnyImplInterface
            
            def set_config_impl(config: Config):
                from $L import $L
                config.dafnyImplInterface = DafnyImplInterface()
                config.dafnyImplInterface.impl = $L()
                config.retry_strategy = NoRetriesStrategy()
            
            class NoRetriesToken:
                retry_delay = 0
            
            class NoRetriesStrategy(RetryStrategy):
                def acquire_initial_retry_token(self):
                    return NoRetriesToken()
            
                def refresh_retry_token_for_retry(self, token_to_renew, error_info):
                    # Do not retry
                    raise SmithyRetryException()
                    """, implModulePrelude, clientName, clientName
            );
        });

        // TODO: StringBuilder
        String operations = "";
        for (OperationShape operationShape : codegenContext.model().getOperationShapes()) {
            operations += """
                "%1$s": self.%2$s.%1$s,\n
                """.formatted(operationShape.getId().getName(), "impl");
        }
        String allOperations = operations;

        // TODO: refactor to DafnyImplInterfaceFileWriter
        // TODO: Naming of this file?
        codegenContext.writerDelegator().useFileWriter(moduleName + "/dafnyImplInterface.py", "", writer -> {
            writer.write(
            """
            from $L import $L
            
            class DafnyImplInterface:
                $L: $L | None = None
            
                def handle_request(self, input):
                
                    # TODO: populate map at runtime (since impl is only populated at runtime, and avoids a None exception),
                    #       but don't re-populate it at every handle_request call, i.e. cache
                    operation_map = {
                        $L
                    }
            
                    operation_name = input[0]
                    return operation_map[operation_name](input[1])
            """, implModulePrelude, clientName, "impl", clientName, allOperations
            );
        });

        // TODO: refactor to DafnyProtocolFileWriter
        // TODO: Naming of this file?
        // I'm not sure how we use this.. maybe for better type checking?
        // maybe something like DafnyInput = Union[forall operations: DafnyName(operation)]
        codegenContext.writerDelegator().useFileWriter(moduleName + "/dafny_protocol.py", "", writer -> {
            writer.write(
                """
                class DafnyRequest:
                    # TODO: smithy-python requires some class for the "application protocol input",
                    # but we do not use this at this time.
                    pass
                    
                class DafnyResponse:
                    # TODO: smithy-python requires some class for the "application protocol output",
                    # but we do not use this at this time.
                    pass
                """
            );
        });

        String typesModulePrelude = serviceShape.getId().getNamespace().toLowerCase(Locale.ROOT) + ".internaldafny.types";
        // TODO: refactor to DafnyProtocolFileWriter
        // TODO: Naming of this file?

        // TODO: StringBuilder
        /*
        TODO: This is what this SHOULD look like after getting some sort of TypeConversion in
                        unwrapped_request = TypeConversion.ToNative(input)
                        try:
                            wrapped_response = self._impl.get_integer(unwrapped_request)
                            return Wrappers_Compile.Result_Success(wrapped_response)
                        catch ex:
                            return Wrappers_Compile.Result_Failure(ex)
         */
        String operationsShim = "";
        String errorsString = "";
        Set<ShapeId> allInputShapesSet = new HashSet<>();
        var deserializingErrorShapes = new TreeSet<ShapeId>();
        var service = codegenContext.settings().getService(codegenContext.model());
        for (OperationShape operationShape : codegenContext.model().getOperationShapes()) {
            deserializingErrorShapes.addAll(operationShape.getErrors(service));
            String inputName = operationShape.getInputShape().getName();
            allInputShapesSet.add(operationShape.getInputShape());
            String doubledInputName = typesModulePrelude + "." + inputName + "_" + inputName;
            String outputName = operationShape.getOutputShape().getName();
            String doubledOutputName = typesModulePrelude + "." + outputName + "_" + outputName;
            String operationSymbol = codegenContext.symbolProvider().toSymbol(operationShape).getName();

            operationsShim += """
                    def %1$s(self, input: %2$s) -> %3$s:
                            unwrapped_request: %4$s = %4$s(value=input.value)
                            try:
                                wrapped_response = asyncio.run(self._impl.%5$s(unwrapped_request))
                            except ServiceError as e:
                                return Wrappers_Compile.Result_Failure(smithy_error_to_dafny_error(e))
                            return Wrappers_Compile.Result_Success(wrapped_response)
                """.formatted(
                    operationShape.getId().getName(),
                doubledInputName,
                doubledOutputName,
                inputName,
                operationSymbol
                );
        }
        String allOperationsShim = operationsShim;

        for (ShapeId errorShape : deserializingErrorShapes) {
            errorsString += """
if isinstance(e, %1$s):
            return %2$s%3$s(message=e.message)
                """.formatted(
                    errorShape.getName(),
                errorShape.getNamespace() + ".internaldafny.types.",
                "Error_" + errorShape.getName()
            );
        }
        final String finalErrorsString = errorsString;

        codegenContext.writerDelegator().useFileWriter(moduleName + "/shim.py", "", writer -> {
            for (ShapeId inputShapeId : allInputShapesSet) {
                writer.addImport(".models", inputShapeId.getName());
            }

            writer.addImport(".errors", "ServiceError");

            for (ShapeId errorShapeId : deserializingErrorShapes) {
                writer.addImport(".errors", errorShapeId.getName());
            }

            writer.write(
                """
                import Wrappers_Compile
                import asyncio
                import $L
                import $L.smithy_generated.$L.client as client_impl
               
                                
                def smithy_error_to_dafny_error(e: ServiceError):
                    $L
                                
                class $L($L.$L):
                    def __init__(self, _impl: client_impl) :
                        self._impl = _impl
                                
                $L
                    
                    """, typesModulePrelude, moduleName, moduleName, finalErrorsString, shimForService(serviceShape),
                typesModulePrelude, "I" + serviceShape.getId().getName() + "Client", allOperationsShim
            );
        });

    }

    /**
     * Creates the Dafny ApplicationProtocol object.
     * This is largely entirely unused boilerplate.
     * Smithy-Python requires this boilerplate, but the Dafny plugin doesn't use it.
     *
     * @return Returns the created application protocol.
     */
    public static ApplicationProtocol createDafnyApplicationProtocol() {
        return new ApplicationProtocol(
            "dafny",
            // TODO: Naming of these symbols?
            SymbolReference.builder()
                .symbol(createDafnySymbol("DafnyRequest"))
                .build(),
            SymbolReference.builder()
                .symbol(createDafnySymbol("DafnyResponse"))
                .build()
        );
    }

    private static Symbol createDafnySymbol(String symbolName) {
        return Symbol.builder()
            .namespace(".dafny_protocol", ".")
            .name(symbolName)
            .build();
    }

    @Override
    public List<ProtocolGenerator> getProtocolGenerators() {
        return Collections.singletonList(new DafnyProtocolGenerator() {
            @Override
            protected void generateDocumentBodyShapeDeserializers(GenerationContext context,
                Set<Shape> shapes) {

            }

            @Override
            public ShapeId getProtocol() {
                return ShapeId.from("aws.polymorph#localService");
            }
        });
    }

    @Override
    public List<RuntimeClientPlugin> getClientPlugins() {
        return Collections.singletonList(dafnyImplRuntimeClientPlugin);
    }
}
