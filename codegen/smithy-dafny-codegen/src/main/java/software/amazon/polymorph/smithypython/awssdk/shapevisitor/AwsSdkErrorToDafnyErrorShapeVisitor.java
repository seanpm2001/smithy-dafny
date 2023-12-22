// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

package software.amazon.polymorph.smithypython.awssdk.shapevisitor;

import software.amazon.polymorph.smithypython.awssdk.nameresolver.AwsSdkNameResolver;
import software.amazon.polymorph.smithypython.awssdk.shapevisitor.conversionwriters.AwsSdkToDafnyConversionFunctionWriter;
import software.amazon.polymorph.smithypython.awssdk.shapevisitor.conversionwriters.DafnyToAwsSdkConversionFunctionWriter;
import software.amazon.polymorph.smithypython.common.nameresolver.SmithyNameResolver;
import software.amazon.polymorph.smithypython.common.nameresolver.Utils;
import software.amazon.smithy.codegen.core.CodegenException;
import software.amazon.smithy.model.shapes.*;
import software.amazon.smithy.model.traits.EnumTrait;
import software.amazon.smithy.model.traits.ErrorTrait;
import software.amazon.smithy.python.codegen.GenerationContext;
import software.amazon.smithy.python.codegen.PythonWriter;

/**
 * ShapeVisitor that should be dispatched from a shape to generate code that maps a AWS SDK
 * kwarg-indexed dictionary to the corresponding Dafny shape's internal attributes.
 */
public class AwsSdkErrorToDafnyErrorShapeVisitor extends ShapeVisitor.Default<String> {
  private final GenerationContext context;
  private String dataSource;
  private final PythonWriter writer;

  /**
   * @param context The generation context.
   * @param dataSource The in-code location of the data to provide an output of ({@code output.foo},
   *     {@code entry}, etc.)
   * @param writer A PythonWriter pointing to the in-code location where the ShapeVisitor was called
   *     from
   */
  public AwsSdkErrorToDafnyErrorShapeVisitor(
      GenerationContext context, String dataSource, PythonWriter writer) {
    this.context = context;
    this.dataSource = dataSource;
    this.writer = writer;
  }

  @Override
  protected String getDefault(Shape shape) {
    String protocolName = context.protocolGenerator().getName();
    throw new CodegenException(
        String.format(
            "Unsupported conversion of %s to %s using the %s protocol",
            shape, shape.getType(), protocolName));
  }

  @Override
  public String blobShape(BlobShape shape) {
    writer.addStdlibImport("_dafny", "Seq");
    return "Seq(" + dataSource + ")";
  }

  @Override
  public String structureShape(StructureShape structureShape) {
    // Dafny does not generate a type for Unit shape
    if (Utils.isUnitShape(structureShape.getId())) {
      return "None";
    }

    if (!structureShape.hasTrait(ErrorTrait.class)) {
      return structureShape.accept(new AwsSdkToDafnyShapeVisitor(context, dataSource, writer));
    }

    AwsSdkToDafnyConversionFunctionWriter.writeConverterForShapeAndMembers(
        structureShape, context, writer);
    DafnyToAwsSdkConversionFunctionWriter.writeConverterForShapeAndMembers(
        structureShape, context, writer);

    // Import the converter from where the ShapeVisitor was called
    String pythonModuleName =
        SmithyNameResolver.getPythonModuleSmithygeneratedPathForSmithyNamespace(
            structureShape.getId().getNamespace(), context);
    writer.addStdlibImport(pythonModuleName + ".aws_sdk_to_dafny");

    // Return a reference to the generated conversion method
    // ex. for shape example.namespace.ExampleShape
    // returns
    // `example_namespace.smithygenerated.aws_sdk_to_dafny.AwsSdkToDafny_example_namespace_ExampleShape(input)`
    return "%1$s.aws_sdk_to_dafny.%2$s(%3$s)"
        .formatted(
            pythonModuleName,
            AwsSdkNameResolver.getAwsSdkToDafnyFunctionNameForShape(structureShape),
            dataSource);
  }

  @Override
  public String listShape(ListShape shape) {
    writer.addStdlibImport("_dafny", "Seq");

    StringBuilder builder = new StringBuilder();

    // Open Dafny sequence:
    // `Seq([`
    builder.append("Seq([");
    MemberShape memberShape = shape.getMember();
    final Shape targetShape = context.model().expectShape(memberShape.getTarget());

    // Add converted list elements into the list:
    // `Seq([`SmithyToDafny(list_element)``
    builder.append(
        "%1$s"
            .formatted(
                targetShape.accept(
                    new AwsSdkErrorToDafnyErrorShapeVisitor(context, "list_element", writer))));

    // Close structure
    // `Seq([`SmithyToDafny(list_element)` for list_element in `dataSource`])``
    return builder.append(" for list_element in %1$s])".formatted(dataSource)).toString();
  }

  @Override
  public String mapShape(MapShape shape) {
    writer.addStdlibImport("_dafny", "Map");

    StringBuilder builder = new StringBuilder();

    // Open Dafny map:
    // `Map({`
    builder.append("Map({");
    MemberShape keyMemberShape = shape.getKey();
    final Shape keyTargetShape = context.model().expectShape(keyMemberShape.getTarget());
    MemberShape valueMemberShape = shape.getValue();
    final Shape valueTargetShape = context.model().expectShape(valueMemberShape.getTarget());

    // Write converted map keys into the map:
    // `{`SmithyToDafny(key)`:`
    builder.append(
        "%1$s: "
            .formatted(
                keyTargetShape.accept(
                    new AwsSdkErrorToDafnyErrorShapeVisitor(context, "key", writer))));

    // Write converted map values into the map:
    // `{`SmithyToDafny(key)`: `SmithyToDafny(value)``
    builder.append(
        "%1$s"
            .formatted(
                valueTargetShape.accept(
                    new AwsSdkErrorToDafnyErrorShapeVisitor(context, "value", writer))));

    // Complete map comprehension and close map
    // `{`SmithyToDafny(key)`: `SmithyToDafny(value)`` for (key, value) in `dataSource`.items() }`
    return builder.append(" for (key, value) in %1$s.items() })".formatted(dataSource)).toString();
  }

  @Override
  public String booleanShape(BooleanShape shape) {
    return dataSource;
  }

  @Override
  public String stringShape(StringShape shape) {
    writer.addStdlibImport("_dafny", "Seq");

    if (shape.hasTrait(EnumTrait.class)) {
      DafnyToAwsSdkConversionFunctionWriter.writeConverterForShapeAndMembers(
          shape, context, writer);
      AwsSdkToDafnyConversionFunctionWriter.writeConverterForShapeAndMembers(
          shape, context, writer);

      // Import the dafny_to_aws_sdk converter from where the ShapeVisitor was called
      String pythonModuleSmithygeneratedPath =
          SmithyNameResolver.getPythonModuleSmithygeneratedPathForSmithyNamespace(
              shape.getId().getNamespace(), context);
      writer.addStdlibImport(pythonModuleSmithygeneratedPath + ".aws_sdk_to_dafny");

      // Return a reference to the generated conversion method
      // ex. for shape example.namespace.ExampleShape
      // returns
      // `example_namespace.smithygenerated.dafny_to_aws_sdk.DafnyToAwsSdk_example_namespace_ExampleShape(input)`
      return "%1$s.aws_sdk_to_dafny.%2$s(%3$s)"
          .formatted(
              pythonModuleSmithygeneratedPath,
              AwsSdkNameResolver.getAwsSdkToDafnyFunctionNameForShape(shape),
              dataSource);
    }

    return "Seq(" + dataSource + ")";
  }

  @Override
  public String byteShape(ByteShape shape) {
    return getDefault(shape);
  }

  @Override
  public String shortShape(ShortShape shape) {
    return getDefault(shape);
  }

  @Override
  public String integerShape(IntegerShape shape) {
    return dataSource;
  }

  @Override
  public String longShape(LongShape shape) {
    return dataSource;
  }

  @Override
  public String bigIntegerShape(BigIntegerShape shape) {
    return getDefault(shape);
  }

  @Override
  public String floatShape(FloatShape shape) {
    return getDefault(shape);
  }

  @Override
  public String doubleShape(DoubleShape shape) {
    return dataSource;
  }

  @Override
  public String bigDecimalShape(BigDecimalShape shape) {
    return getDefault(shape);
  }

  @Override
  public String enumShape(EnumShape shape) {
    return dataSource;
  }

  @Override
  public String timestampShape(TimestampShape shape) {
    // TODO-Python BLOCKING: This lets code generate, but will fail when code uses it
    return "TypeError(\"TimestampShape not supported\")";
  }

  @Override
  public String unionShape(UnionShape unionShape) {
    DafnyToAwsSdkConversionFunctionWriter.writeConverterForShapeAndMembers(
        unionShape, context, writer);
    AwsSdkToDafnyConversionFunctionWriter.writeConverterForShapeAndMembers(
        unionShape, context, writer);

    // Import the converter from where the ShapeVisitor was called
    String pythonModuleName =
        SmithyNameResolver.getPythonModuleSmithygeneratedPathForSmithyNamespace(
            unionShape.getId().getNamespace(), context);
    writer.addStdlibImport(pythonModuleName + ".aws_sdk_to_dafny");

    // Return a reference to the generated conversion method
    // ex. for shape example.namespace.ExampleShape
    // returns
    // `example_namespace.smithygenerated.aws_sdk_to_dafny.AwsSdkToDafny_example_namespace_ExampleShape(input)`
    return "%1$s.aws_sdk_to_dafny.%2$s(%3$s)"
        .formatted(
            pythonModuleName,
            AwsSdkNameResolver.getAwsSdkToDafnyFunctionNameForShape(unionShape),
            dataSource);
  }
}
