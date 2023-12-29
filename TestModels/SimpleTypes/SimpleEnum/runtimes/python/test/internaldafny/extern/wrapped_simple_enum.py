# Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0

# TODO-Python-PYTHONPATH: Qualify imports
import simple_types_smithyenum_internaldafny_wrapped
from simple_types_smithyenum.smithygenerated.simple_types_smithyenum.client import SimpleTypesEnum
from simple_types_smithyenum.smithygenerated.simple_types_smithyenum.shim import SimpleEnumShim
from simple_types_smithyenum.smithygenerated.simple_types_smithyenum.config import dafny_config_to_smithy_config
import Wrappers

class default__(simple_types_smithyenum_internaldafny_wrapped.default__):

    @staticmethod
    def WrappedSimpleEnum(config):
        wrapped_config = dafny_config_to_smithy_config(config)
        impl = SimpleTypesEnum(wrapped_config)
        wrapped_client = SimpleEnumShim(impl)
        return Wrappers.Result_Success(wrapped_client)

# (TODO-Python-PYTHONPATH: Remove)
simple_types_smithyenum_internaldafny_wrapped.default__ = default__
