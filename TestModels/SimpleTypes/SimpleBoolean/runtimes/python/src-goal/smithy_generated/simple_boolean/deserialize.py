# Code generated by smithy-python-codegen DO NOT EDIT.

from simple.types.boolean.internaldafny.types import (
    GetBooleanOutput_GetBooleanOutput as DafnyGetBooleanOutput,
)

from .config import Config
from .models import GetBooleanOutput


async def _deserialize_get_boolean(input: DafnyGetBooleanOutput, config: Config) -> GetBooleanOutput:

  return GetBooleanOutput(value=input.value.value)
