# Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0

# TODO-Python-PYTHONPATH: Qualify imports
import simple_types_smithylong_internaldafny_wrapped
from simple_types_smithylong.smithygenerated.simple_types_smithylong.client import SimpleTypesLong
from simple_types_smithylong.smithygenerated.simple_types_smithylong.shim import SimpleLongShim
from simple_types_smithylong.smithygenerated.simple_types_smithylong.config import dafny_config_to_smithy_config
import Wrappers

class default__(simple_types_smithylong_internaldafny_wrapped.default__):

    @staticmethod
    def WrappedSimpleLong(config):
        wrapped_config = dafny_config_to_smithy_config(config)
        impl = SimpleTypesLong(wrapped_config)
        wrapped_client = SimpleLongShim(impl)
        return Wrappers.Result_Success(wrapped_client)

# (TODO-Python-PYTHONPATH: Remove)
simple_types_smithylong_internaldafny_wrapped.default__ = default__
