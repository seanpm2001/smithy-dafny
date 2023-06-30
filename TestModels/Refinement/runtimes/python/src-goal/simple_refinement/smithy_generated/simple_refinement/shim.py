# Code generated by smithy-python-codegen DO NOT EDIT.

from .errors import ServiceError
from .models import GetRefinementInput, OnlyInputInput, ReadonlyOperationInput
from simple.refinement.internaldafny.types import (
  GetRefinementOutput_GetRefinementOutput as DafnyGetRefinementOutput,
  ReadonlyOperationOutput_ReadonlyOperationOutput as DafnyReadonlyOperationOutput,
)

import Wrappers_Compile
import asyncio
import simple.refinement.internaldafny.types
import simple_refinement.smithy_generated.simple_refinement.client as client_impl


class SimpleRefinementShim(simple.refinement.internaldafny.types.ISimpleRefinementClient):
    def __init__(self, _impl: client_impl) :
        self._impl = _impl

    def OnlyOutput(self,) -> simple.refinement.internaldafny.types.OnlyOutputOutput_OnlyOutputOutput:
            unwrapped_request = None
            try:
                wrapped_response = asyncio.run(self._impl.only_output(unwrapped_request))
            except ServiceError as e:
                return Wrappers_Compile.Result_Failure(smithy_error_to_dafny_error(e))
            return Wrappers_Compile.Result_Success(wrapped_response)
    def OnlyInput(self, input: simple.refinement.internaldafny.types.OnlyInputInput_OnlyInputInput) -> None:
            unwrapped_request: OnlyInputInput = OnlyInputInput()
            try:
                wrapped_response = asyncio.run(self._impl.only_input(unwrapped_request))
            except ServiceError as e:
                return Wrappers_Compile.Result_Failure(smithy_error_to_dafny_error(e))
            return Wrappers_Compile.Result_Success(wrapped_response)
    def ReadonlyOperation(self, input: simple.refinement.internaldafny.types.ReadonlyOperationInput_ReadonlyOperationInput) -> simple.refinement.internaldafny.types.ReadonlyOperationOutput_ReadonlyOperationOutput:
            unwrapped_request: ReadonlyOperationInput = ReadonlyOperationInput(required_string=input.requiredString,
                                                                               optional_string=input.optionalString)
            try:
                wrapped_response = asyncio.run(self._impl.readonly_operation(unwrapped_request))
            except ServiceError as e:
                return Wrappers_Compile.Result_Failure(smithy_error_to_dafny_error(e))
            return Wrappers_Compile.Result_Success(DafnyReadonlyOperationOutput(requiredString=wrapped_response.required_string,
                                                                                optionalString=wrapped_response.optional_string))
    def GetRefinement(self, input: simple.refinement.internaldafny.types.GetRefinementInput_GetRefinementInput) -> simple.refinement.internaldafny.types.GetRefinementOutput_GetRefinementOutput:
            unwrapped_request: GetRefinementInput = GetRefinementInput(required_string=input.requiredString,
                                                                       optional_string=input.optionalString)
            try:
                wrapped_response = asyncio.run(self._impl.get_refinement(unwrapped_request))
                print("wrapped_response")
                print(wrapped_response)
            except ServiceError as e:
                return Wrappers_Compile.Result_Failure(smithy_error_to_dafny_error(e))
            return Wrappers_Compile.Result_Success(DafnyGetRefinementOutput(requiredString=wrapped_response.required_string,
                                                                            optionalString=wrapped_response.optional_string))
