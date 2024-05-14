# Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0

# Initialize generated Dafny
import simple_dafnyextern.internaldafny.generated.module_

# Initialize externs
from . import ExternConstructor
from . import SimpleExternImpl

# If this is the first Dafny module to load,
# set this as the main module for the DafnyRuntime package
try:
    import module_
except ImportError:
    import sys
    sys.modules["module_"] = simple_dafnyextern.internaldafny.generated.module_
