// Copyright Amazon.com Inc. or its affiliates. All Rights Reserved.
// SPDX-License-Identifier: Apache-2.0

// Something like this should work once we implement the
// "dafny-client-codegen" Smithy build plugin and
// configure it in smithy-build.json.
// Note the lack of any manually-written code in the project!

include "../src/Index.dfy"

module TestComAmazonawsSqs {
  import Com.Amazonaws.Sqs
  import opened StandardLibrary.UInt
  import opened Wrappers

  method BasicSanityTest()
  {
    var client :- expect Sqs.SQSClient();

    var ret :- expect client.ListQueues(input);

    var ListQueuesResult(QueueUrls) := ret;

    expect QueueUrls.Some?;
    expect |QueueUrls.value| == 0;
  }
}