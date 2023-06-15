# Code generated by smithy-python-codegen DO NOT EDIT.

from asyncio import sleep
from copy import deepcopy
from typing import Awaitable, Callable, TypeVar, cast

from .plugin import set_config_impl
from simple.types.boolean.internaldafny.types import (
    GetBooleanInput_GetBooleanInput,
    GetBooleanOutput_GetBooleanOutput,
)
from smithy_python.exceptions import SmithyRetryException
from smithy_python.interfaces.interceptor import Interceptor, InterceptorContext
from smithy_python.interfaces.retries import RetryErrorInfo, RetryErrorType

from .config import Config, Plugin
from .deserialize import _deserialize_get_boolean
from .errors import ServiceError
from .models import GetBooleanInput, GetBooleanOutput
from .serialize import _serialize_get_boolean


Input = TypeVar("Input")
Output = TypeVar("Output")

class SimpleBoolean:
    """Client for SimpleBoolean

    :param config: Optional configuration for the client. Here you can set things like the
    endpoint for HTTP services or auth credentials.

    :param plugins: A list of callables that modify the configuration dynamically. These
    can be used to set defaults, for example.
    """
    def __init__(self, config: Config | None = None, plugins: list[Plugin] | None = None):
        self._config = config or Config()

        client_plugins: list[Plugin] = [
            set_config_impl,
        ]
        if plugins:
            client_plugins.extend(plugins)

        for plugin in client_plugins:
            plugin(self._config)

    async def get_boolean(self, input: GetBooleanInput, plugins: list[Plugin] | None = None) -> GetBooleanOutput:
        """Invokes the GetBoolean operation.

        :param input: The operation's input.

        :param plugins: A list of callables that modify the configuration dynamically.
        Changes made by these plugins only apply for the duration of the operation
        execution and will not affect any other operation invocations.
        """
        operation_plugins = [

        ]
        if plugins:
            operation_plugins.extend(plugins)

        return await self._execute_operation(
            input=input,
            plugins=operation_plugins,
            serialize=_serialize_get_boolean,
            deserialize=_deserialize_get_boolean,
            config=self._config,
        )

    async def _execute_operation(
        self,
        input: Input,
        plugins: list[Plugin],
        serialize: Callable[[Input, Config], Awaitable[GetBooleanOutput_GetBooleanOutput]],
        deserialize: Callable[[GetBooleanInput_GetBooleanInput, Config], Awaitable[Output]],
        config: Config,
    ) -> Output:
        try:
            return await self._handle_execution(
                input, plugins, serialize, deserialize, config
            )
        except Exception as e:
            # Make sure every exception that we throw is an instance of ServiceError so
            # customers can reliably catch everything we throw.
            if not isinstance(e, ServiceError):
                raise ServiceError(e) from e
            raise e

    async def _handle_execution(
        self,
        input: Input,
        plugins: list[Plugin],
        serialize: Callable[[Input, Config], Awaitable[GetBooleanOutput_GetBooleanOutput]],
        deserialize: Callable[[GetBooleanInput_GetBooleanInput, Config], Awaitable[Output]],
        config: Config,
    ) -> Output:
        context: InterceptorContext[Input, None, None, None] = InterceptorContext(
            request=input,
            response=None,
            transport_request=None,
            transport_response=None,
        )
        _client_interceptors = config.interceptors or []
        client_interceptors = cast(
            list[Interceptor[Input, Output, GetBooleanOutput_GetBooleanOutput, GetBooleanInput_GetBooleanInput]], _client_interceptors
        )
        interceptors = client_interceptors

        try:
            # Step 1a: Invoke read_before_execution on client-level interceptors
            for interceptor in client_interceptors:
                interceptor.read_before_execution(context)

            # Step 1b: Run operation-level plugins
            config = deepcopy(config)
            for plugin in plugins:
                plugin(config)

            _client_interceptors = config.interceptors or []
            interceptors = cast(
                list[Interceptor[Input, Output, GetBooleanOutput_GetBooleanOutput, GetBooleanInput_GetBooleanInput]],
                _client_interceptors,
            )

            # Step 1c: Invoke the read_before_execution hooks on newly added
            # interceptors.
            for interceptor in interceptors:
                if interceptor not in client_interceptors:
                    interceptor.read_before_execution(context)

            # Step 2: Invoke the modify_before_serialization hooks
            for interceptor in interceptors:
                context._request = interceptor.modify_before_serialization(context)

            # Step 3: Invoke the read_before_serialization hooks
            for interceptor in interceptors:
                interceptor.read_before_serialization(context)

            # Step 4: Serialize the request
            context_with_transport_request = cast(
                InterceptorContext[Input, None, GetBooleanOutput_GetBooleanOutput, None], context
            )
            context_with_transport_request._transport_request = await serialize(
                context_with_transport_request.request, config
            )

            # Step 5: Invoke read_after_serialization
            for interceptor in interceptors:
                interceptor.read_after_serialization(context_with_transport_request)

            # Step 6: Invoke modify_before_retry_loop
            for interceptor in interceptors:
                context_with_transport_request._transport_request = (
                    interceptor.modify_before_retry_loop(context_with_transport_request)
                )

            # Step 7: Acquire the retry token.
            retry_strategy = config.retry_strategy
            if retry_strategy is None:
                raise ServiceError(
                    "No retry_strategy found on the operation config."
                )
            retry_token = retry_strategy.acquire_initial_retry_token()

            while True:
                # Make an attempt, creating a copy of the context so we don't pass
                # around old data.
                context_with_response = await self._handle_attempt(
                    deserialize,
                    interceptors,
                    context_with_transport_request.copy(),
                    config,
                )

                # We perform this type-ignored re-assignment because `context` needs
                # to point at the latest context so it can be generically handled
                # later on. This is only an issue here because we've created a copy,
                # so we're no longer simply pointing at the same object in memory
                # with different names and type hints. It is possible to address this
                # without having to fall back to the type ignore, but it would impose
                # unnecessary runtime costs.
                context = context_with_response  # type: ignore

                if isinstance(context_with_response.response, Exception):
                    # Step 7u: Reacquire retry token if the attempt failed
                    try:
                        retry_token = retry_strategy.refresh_retry_token_for_retry(
                            token_to_renew=retry_token,
                            error_info=RetryErrorInfo(
                                # TODO: Determine the error type.
                                error_type=RetryErrorType.CLIENT_ERROR,
                            )
                        )
                    except SmithyRetryException:
                        raise context_with_response.response
                    await sleep(retry_token.retry_delay)
                else:
                    # Step 8: Invoke record_success
                    retry_strategy.record_success(token=retry_token)
                    break
        except Exception as e:
            if context.response is not None:
                # config.logger.exception(f"Exception occurred while handling: {context.response}")
                pass
            context._response = e

        # At this point, the context's request will have been definitively set, and
        # The response will be set either with the modeled output or an exception. The
        # transport_request and transport_response may be set or None.
        execution_context = cast(
            InterceptorContext[Input, Output, GetBooleanOutput_GetBooleanOutput | None, GetBooleanInput_GetBooleanInput | None], context
        )
        return await self._finalize_execution(interceptors, execution_context)

    async def _handle_attempt(
        self,
        deserialize: Callable[[GetBooleanInput_GetBooleanInput, Config], Awaitable[Output]],
        interceptors: list[Interceptor[Input, Output, GetBooleanOutput_GetBooleanOutput, GetBooleanInput_GetBooleanInput]],
        context: InterceptorContext[Input, None, GetBooleanOutput_GetBooleanOutput, None],
        config: Config,
    ) -> InterceptorContext[Input, Output, GetBooleanOutput_GetBooleanOutput, GetBooleanInput_GetBooleanInput | None]:
        try:
            # assert config.interceptors is not None
            # Step 7a: Invoke read_before_attempt
            for interceptor in interceptors:
                interceptor.read_before_attempt(context)

            # Steps 7b-e haven't had their python designs finalized yet
            # Step 7b: Invoke service_auth_scheme_resolver.resolve_auth_scheme
            # Step 7c: Invoke auth_scheme.identity_resolver
            # Step 7d: Invoke auth_scheme.signer
            # Step 7e: Invoke identity_resolver.resolve_identity

            # Step 7g: Invoke modify_before_signing
            for interceptor in interceptors:
                context._transport_request = interceptor.modify_before_signing(context)

            # Step 7h: Invoke read_before_signing
            for interceptor in interceptors:
                interceptor.read_before_signing(context)

            # Step 7i: Invoke signer.sign_request
            # This step hasn't had its python design finalized yet

            # Step 7j: Invoke read_after_signing
            for interceptor in interceptors:
                interceptor.read_after_signing(context)

            # Step 7k: Invoke modify_before_transmit
            for interceptor in interceptors:
                context._transport_request = interceptor.modify_before_transmit(context)

            # Step 7l: Invoke read_before_transmit
            for interceptor in interceptors:
                interceptor.read_before_transmit(context)

            ## HERE
            # Step 7m: Invoke http_client.send
            if config.impl is None:
                raise Exception("No impl found on the operation config.")

            context_with_response = cast(
                InterceptorContext[Input, None,  GetBooleanInput_GetBooleanInput, GetBooleanOutput_GetBooleanOutput], context
            )

            print(f"transport_request is {context_with_response.transport_request}")

            context_with_response._transport_response = config.impl.GetBoolean(
                input=context_with_response.transport_request
            )

            # Step 7n: Invoke read_after_transmit
            for interceptor in interceptors:
                interceptor.read_after_transmit(context_with_response)

            # Step 7o: Invoke modify_before_deserialization
            for interceptor in interceptors:
                context_with_response._transport_response = (
                    interceptor.modify_before_deserialization(context_with_response)
                )

            # Step 7p: Invoke read_before_deserialization
            for interceptor in interceptors:
                interceptor.read_before_deserialization(context_with_response)

            # Step 7q: deserialize
            context_with_output = cast(
                InterceptorContext[Input, Output, GetBooleanOutput_GetBooleanOutput, GetBooleanInput_GetBooleanInput],
                context_with_response,
            )
            context_with_output._response = await deserialize(
                context_with_output._transport_response, config
            )

            # Step 7r: Invoke read_after_deserialization
            for interceptor in interceptors:
                interceptor.read_after_deserialization(context_with_output)
        except Exception as e:
            if context.response is not None:
                # config.logger.exception(f"Exception occurred while handling: {context.response}")
                pass
            context._response = e

        # At this point, the context's request and transport_request have definitively been set,
        # the response is either set or an exception, and the transport_resposne is either set or
        # None. This will also be true after _finalize_attempt because there is no opportunity
        # there to set the transport_response.
        attempt_context = cast(
            InterceptorContext[Input, Output, GetBooleanOutput_GetBooleanOutput, GetBooleanInput_GetBooleanInput | None], context
        )
        return await self._finalize_attempt(interceptors, attempt_context)

    async def _finalize_attempt(
        self,
        interceptors: list[Interceptor[Input, Output, GetBooleanOutput_GetBooleanOutput, GetBooleanInput_GetBooleanInput]],
        context: InterceptorContext[Input, Output, GetBooleanOutput_GetBooleanOutput, GetBooleanInput_GetBooleanInput | None],
    ) -> InterceptorContext[Input, Output, GetBooleanOutput_GetBooleanOutput, GetBooleanInput_GetBooleanInput | None]:
        # Step 7s: Invoke modify_before_attempt_completion
        try:
            for interceptor in interceptors:
                context._response = interceptor.modify_before_attempt_completion(
                    context
                )
        except Exception as e:
            if context.response is not None:
                # config.logger.exception(f"Exception occurred while handling: {context.response}")
                pass
            context._response = e

        # Step 7t: Invoke read_after_attempt
        for interceptor in interceptors:
            try:
                interceptor.read_after_attempt(context)
            except Exception as e:
                if context.response is not None:
                    # config.logger.exception(f"Exception occurred while handling: {context.response}")
                    pass
                context._response = e

        return context

    async def _finalize_execution(
        self,
        interceptors: list[Interceptor[Input, Output, GetBooleanOutput_GetBooleanOutput, GetBooleanInput_GetBooleanInput]],
        context: InterceptorContext[Input, Output, GetBooleanOutput_GetBooleanOutput | None, GetBooleanInput_GetBooleanInput | None],
    ) -> Output:
        try:
            # Step 9: Invoke modify_before_completion
            for interceptor in interceptors:
                context._response = interceptor.modify_before_completion(context)

            # Step 10: Invoke trace_probe.dispatch_events
            try:
                pass
            except Exception as e:
                # log and ignore exceptions
                # config.logger.exception(f"Exception occurred while dispatching trace events: {e}")
                pass
        except Exception as e:
            if context.response is not None:
                # config.logger.exception(f"Exception occurred while handling: {context.response}")
                pass
            context._response = e

        # Step 11: Invoke read_after_execution
        for interceptor in interceptors:
            try:
                interceptor.read_after_execution(context)
            except Exception as e:
                if context.response is not None:
                    # config.logger.exception(f"Exception occurred while handling: {context.response}")
                    pass
                context._response = e

        # Step 12: Return / throw
        if isinstance(context.response, Exception):
            raise context.response

        # We may want to add some aspects of this context to the output types so we can
        # return it to the end-users.
        return context.response
