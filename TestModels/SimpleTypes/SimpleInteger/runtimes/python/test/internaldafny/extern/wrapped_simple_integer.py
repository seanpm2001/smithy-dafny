# Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0

# TODO-Python-PYTHONPATH: Qualify imports
import simple_types_integer_internaldafny_wrapped
from simple_types_integer.smithygenerated.simple_types_integer.client import SimpleTypesInteger
from simple_types_integer.smithygenerated.simple_types_integer.shim import SimpleIntegerShim
from simple_types_integer.smithygenerated.simple_types_integer.config import dafny_config_to_smithy_config
import Wrappers

class default__(simple_types_integer_internaldafny_wrapped.default__):

    @staticmethod
    def WrappedSimpleInteger(config):
        wrapped_config = dafny_config_to_smithy_config(config)
        impl = SimpleTypesInteger(wrapped_config)
        wrapped_client = SimpleIntegerShim(impl)
        return Wrappers.Result_Success(wrapped_client)

# (TODO-Python-PYTHONPATH: Remove)
simple_types_integer_internaldafny_wrapped.default__ = default__
