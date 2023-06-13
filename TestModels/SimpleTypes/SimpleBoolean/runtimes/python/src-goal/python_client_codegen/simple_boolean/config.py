# Code generated by smithy-python-codegen DO NOT EDIT.

from dataclasses import dataclass
from typing import Any, Callable, TypeAlias, Union

import simple.types.boolean.internaldafny.impl

from .models import GetBooleanInput, GetBooleanOutput


@dataclass(kw_only=True)
class Config:
    """Configuration for SimpleBoolean

    :param interceptors: The list of interceptors, which are hooks that are called
    during the execution of a request.

    :param retry_strategy: The retry strategy for issuing retry tokens and computing
    retry delays.

    :param impl:
    """
    interceptors: list[None]
    retry_strategy: None
    impl: simple.types.boolean.internaldafny.impl.SimpleBooleanClient

# A callable that allows customizing the config object on each request.
Plugin: TypeAlias = Callable[[Config], None]
