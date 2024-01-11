# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from flyteidl.artifact import artifacts_pb2 as flyteidl_dot_artifact_dot_artifacts__pb2


class ArtifactRegistryStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.CreateArtifact = channel.unary_unary(
                '/flyteidl.artifact.ArtifactRegistry/CreateArtifact',
                request_serializer=flyteidl_dot_artifact_dot_artifacts__pb2.CreateArtifactRequest.SerializeToString,
                response_deserializer=flyteidl_dot_artifact_dot_artifacts__pb2.CreateArtifactResponse.FromString,
                )
        self.GetArtifact = channel.unary_unary(
                '/flyteidl.artifact.ArtifactRegistry/GetArtifact',
                request_serializer=flyteidl_dot_artifact_dot_artifacts__pb2.GetArtifactRequest.SerializeToString,
                response_deserializer=flyteidl_dot_artifact_dot_artifacts__pb2.GetArtifactResponse.FromString,
                )
        self.SearchArtifacts = channel.unary_unary(
                '/flyteidl.artifact.ArtifactRegistry/SearchArtifacts',
                request_serializer=flyteidl_dot_artifact_dot_artifacts__pb2.SearchArtifactsRequest.SerializeToString,
                response_deserializer=flyteidl_dot_artifact_dot_artifacts__pb2.SearchArtifactsResponse.FromString,
                )
        self.CreateTrigger = channel.unary_unary(
                '/flyteidl.artifact.ArtifactRegistry/CreateTrigger',
                request_serializer=flyteidl_dot_artifact_dot_artifacts__pb2.CreateTriggerRequest.SerializeToString,
                response_deserializer=flyteidl_dot_artifact_dot_artifacts__pb2.CreateTriggerResponse.FromString,
                )
        self.DeactivateTrigger = channel.unary_unary(
                '/flyteidl.artifact.ArtifactRegistry/DeactivateTrigger',
                request_serializer=flyteidl_dot_artifact_dot_artifacts__pb2.DeactivateTriggerRequest.SerializeToString,
                response_deserializer=flyteidl_dot_artifact_dot_artifacts__pb2.DeactivateTriggerResponse.FromString,
                )
        self.AddTag = channel.unary_unary(
                '/flyteidl.artifact.ArtifactRegistry/AddTag',
                request_serializer=flyteidl_dot_artifact_dot_artifacts__pb2.AddTagRequest.SerializeToString,
                response_deserializer=flyteidl_dot_artifact_dot_artifacts__pb2.AddTagResponse.FromString,
                )
        self.RegisterProducer = channel.unary_unary(
                '/flyteidl.artifact.ArtifactRegistry/RegisterProducer',
                request_serializer=flyteidl_dot_artifact_dot_artifacts__pb2.RegisterProducerRequest.SerializeToString,
                response_deserializer=flyteidl_dot_artifact_dot_artifacts__pb2.RegisterResponse.FromString,
                )
        self.RegisterConsumer = channel.unary_unary(
                '/flyteidl.artifact.ArtifactRegistry/RegisterConsumer',
                request_serializer=flyteidl_dot_artifact_dot_artifacts__pb2.RegisterConsumerRequest.SerializeToString,
                response_deserializer=flyteidl_dot_artifact_dot_artifacts__pb2.RegisterResponse.FromString,
                )
        self.SetExecutionInputs = channel.unary_unary(
                '/flyteidl.artifact.ArtifactRegistry/SetExecutionInputs',
                request_serializer=flyteidl_dot_artifact_dot_artifacts__pb2.ExecutionInputsRequest.SerializeToString,
                response_deserializer=flyteidl_dot_artifact_dot_artifacts__pb2.ExecutionInputsResponse.FromString,
                )
        self.FindByWorkflowExec = channel.unary_unary(
                '/flyteidl.artifact.ArtifactRegistry/FindByWorkflowExec',
                request_serializer=flyteidl_dot_artifact_dot_artifacts__pb2.FindByWorkflowExecRequest.SerializeToString,
                response_deserializer=flyteidl_dot_artifact_dot_artifacts__pb2.SearchArtifactsResponse.FromString,
                )
        self.ListUsage = channel.unary_unary(
                '/flyteidl.artifact.ArtifactRegistry/ListUsage',
                request_serializer=flyteidl_dot_artifact_dot_artifacts__pb2.ListUsageRequest.SerializeToString,
                response_deserializer=flyteidl_dot_artifact_dot_artifacts__pb2.ListUsageResponse.FromString,
                )


class ArtifactRegistryServicer(object):
    """Missing associated documentation comment in .proto file."""

    def CreateArtifact(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetArtifact(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SearchArtifacts(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateTrigger(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeactivateTrigger(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddTag(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RegisterProducer(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def RegisterConsumer(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def SetExecutionInputs(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def FindByWorkflowExec(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ListUsage(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ArtifactRegistryServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'CreateArtifact': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateArtifact,
                    request_deserializer=flyteidl_dot_artifact_dot_artifacts__pb2.CreateArtifactRequest.FromString,
                    response_serializer=flyteidl_dot_artifact_dot_artifacts__pb2.CreateArtifactResponse.SerializeToString,
            ),
            'GetArtifact': grpc.unary_unary_rpc_method_handler(
                    servicer.GetArtifact,
                    request_deserializer=flyteidl_dot_artifact_dot_artifacts__pb2.GetArtifactRequest.FromString,
                    response_serializer=flyteidl_dot_artifact_dot_artifacts__pb2.GetArtifactResponse.SerializeToString,
            ),
            'SearchArtifacts': grpc.unary_unary_rpc_method_handler(
                    servicer.SearchArtifacts,
                    request_deserializer=flyteidl_dot_artifact_dot_artifacts__pb2.SearchArtifactsRequest.FromString,
                    response_serializer=flyteidl_dot_artifact_dot_artifacts__pb2.SearchArtifactsResponse.SerializeToString,
            ),
            'CreateTrigger': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateTrigger,
                    request_deserializer=flyteidl_dot_artifact_dot_artifacts__pb2.CreateTriggerRequest.FromString,
                    response_serializer=flyteidl_dot_artifact_dot_artifacts__pb2.CreateTriggerResponse.SerializeToString,
            ),
            'DeactivateTrigger': grpc.unary_unary_rpc_method_handler(
                    servicer.DeactivateTrigger,
                    request_deserializer=flyteidl_dot_artifact_dot_artifacts__pb2.DeactivateTriggerRequest.FromString,
                    response_serializer=flyteidl_dot_artifact_dot_artifacts__pb2.DeactivateTriggerResponse.SerializeToString,
            ),
            'AddTag': grpc.unary_unary_rpc_method_handler(
                    servicer.AddTag,
                    request_deserializer=flyteidl_dot_artifact_dot_artifacts__pb2.AddTagRequest.FromString,
                    response_serializer=flyteidl_dot_artifact_dot_artifacts__pb2.AddTagResponse.SerializeToString,
            ),
            'RegisterProducer': grpc.unary_unary_rpc_method_handler(
                    servicer.RegisterProducer,
                    request_deserializer=flyteidl_dot_artifact_dot_artifacts__pb2.RegisterProducerRequest.FromString,
                    response_serializer=flyteidl_dot_artifact_dot_artifacts__pb2.RegisterResponse.SerializeToString,
            ),
            'RegisterConsumer': grpc.unary_unary_rpc_method_handler(
                    servicer.RegisterConsumer,
                    request_deserializer=flyteidl_dot_artifact_dot_artifacts__pb2.RegisterConsumerRequest.FromString,
                    response_serializer=flyteidl_dot_artifact_dot_artifacts__pb2.RegisterResponse.SerializeToString,
            ),
            'SetExecutionInputs': grpc.unary_unary_rpc_method_handler(
                    servicer.SetExecutionInputs,
                    request_deserializer=flyteidl_dot_artifact_dot_artifacts__pb2.ExecutionInputsRequest.FromString,
                    response_serializer=flyteidl_dot_artifact_dot_artifacts__pb2.ExecutionInputsResponse.SerializeToString,
            ),
            'FindByWorkflowExec': grpc.unary_unary_rpc_method_handler(
                    servicer.FindByWorkflowExec,
                    request_deserializer=flyteidl_dot_artifact_dot_artifacts__pb2.FindByWorkflowExecRequest.FromString,
                    response_serializer=flyteidl_dot_artifact_dot_artifacts__pb2.SearchArtifactsResponse.SerializeToString,
            ),
            'ListUsage': grpc.unary_unary_rpc_method_handler(
                    servicer.ListUsage,
                    request_deserializer=flyteidl_dot_artifact_dot_artifacts__pb2.ListUsageRequest.FromString,
                    response_serializer=flyteidl_dot_artifact_dot_artifacts__pb2.ListUsageResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'flyteidl.artifact.ArtifactRegistry', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ArtifactRegistry(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def CreateArtifact(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/flyteidl.artifact.ArtifactRegistry/CreateArtifact',
            flyteidl_dot_artifact_dot_artifacts__pb2.CreateArtifactRequest.SerializeToString,
            flyteidl_dot_artifact_dot_artifacts__pb2.CreateArtifactResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetArtifact(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/flyteidl.artifact.ArtifactRegistry/GetArtifact',
            flyteidl_dot_artifact_dot_artifacts__pb2.GetArtifactRequest.SerializeToString,
            flyteidl_dot_artifact_dot_artifacts__pb2.GetArtifactResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SearchArtifacts(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/flyteidl.artifact.ArtifactRegistry/SearchArtifacts',
            flyteidl_dot_artifact_dot_artifacts__pb2.SearchArtifactsRequest.SerializeToString,
            flyteidl_dot_artifact_dot_artifacts__pb2.SearchArtifactsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateTrigger(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/flyteidl.artifact.ArtifactRegistry/CreateTrigger',
            flyteidl_dot_artifact_dot_artifacts__pb2.CreateTriggerRequest.SerializeToString,
            flyteidl_dot_artifact_dot_artifacts__pb2.CreateTriggerResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeactivateTrigger(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/flyteidl.artifact.ArtifactRegistry/DeactivateTrigger',
            flyteidl_dot_artifact_dot_artifacts__pb2.DeactivateTriggerRequest.SerializeToString,
            flyteidl_dot_artifact_dot_artifacts__pb2.DeactivateTriggerResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AddTag(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/flyteidl.artifact.ArtifactRegistry/AddTag',
            flyteidl_dot_artifact_dot_artifacts__pb2.AddTagRequest.SerializeToString,
            flyteidl_dot_artifact_dot_artifacts__pb2.AddTagResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RegisterProducer(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/flyteidl.artifact.ArtifactRegistry/RegisterProducer',
            flyteidl_dot_artifact_dot_artifacts__pb2.RegisterProducerRequest.SerializeToString,
            flyteidl_dot_artifact_dot_artifacts__pb2.RegisterResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def RegisterConsumer(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/flyteidl.artifact.ArtifactRegistry/RegisterConsumer',
            flyteidl_dot_artifact_dot_artifacts__pb2.RegisterConsumerRequest.SerializeToString,
            flyteidl_dot_artifact_dot_artifacts__pb2.RegisterResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def SetExecutionInputs(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/flyteidl.artifact.ArtifactRegistry/SetExecutionInputs',
            flyteidl_dot_artifact_dot_artifacts__pb2.ExecutionInputsRequest.SerializeToString,
            flyteidl_dot_artifact_dot_artifacts__pb2.ExecutionInputsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def FindByWorkflowExec(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/flyteidl.artifact.ArtifactRegistry/FindByWorkflowExec',
            flyteidl_dot_artifact_dot_artifacts__pb2.FindByWorkflowExecRequest.SerializeToString,
            flyteidl_dot_artifact_dot_artifacts__pb2.SearchArtifactsResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ListUsage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/flyteidl.artifact.ArtifactRegistry/ListUsage',
            flyteidl_dot_artifact_dot_artifacts__pb2.ListUsageRequest.SerializeToString,
            flyteidl_dot_artifact_dot_artifacts__pb2.ListUsageResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
