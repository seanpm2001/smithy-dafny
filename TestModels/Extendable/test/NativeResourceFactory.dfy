// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

include "../src/Index.dfy"

module
  {:extern "simple_extendable_resources_internaldafny_nativeresourcefactory"}
  NativeResourceFactory
{
  import Types = SimpleExtendableResourcesTypes
  
  method {:extern "DafnyFactory"} DafnyFactory()
    returns (output: Types.IExtendableResource)
    ensures output.ValidState() && fresh(output.History) && fresh(output.Modifies)  
}
