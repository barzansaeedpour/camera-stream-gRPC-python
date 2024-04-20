# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import images_pb2 as images__pb2


class ImagesStub(object):
    """The greeting service definition.

    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.GetImages = channel.unary_unary(
                '/images.Images/GetImages',
                request_serializer=images__pb2.GetImagesRequest.SerializeToString,
                response_deserializer=images__pb2.GetImagesResponse.FromString,
                )
        self.GetImageById = channel.unary_unary(
                '/images.Images/GetImageById',
                request_serializer=images__pb2.GetImageByIdRequest.SerializeToString,
                response_deserializer=images__pb2.GetImageByIdResponse.FromString,
                )
        self.CreateImage = channel.unary_unary(
                '/images.Images/CreateImage',
                request_serializer=images__pb2.CreateImageRequest.SerializeToString,
                response_deserializer=images__pb2.CreateImageResponse.FromString,
                )
        self.UpdateImage = channel.unary_unary(
                '/images.Images/UpdateImage',
                request_serializer=images__pb2.UpdateImageRequest.SerializeToString,
                response_deserializer=images__pb2.UpdateImageResponse.FromString,
                )
        self.DeleteImage = channel.unary_unary(
                '/images.Images/DeleteImage',
                request_serializer=images__pb2.DeleteImageRequest.SerializeToString,
                response_deserializer=images__pb2.DeleteImageResponse.FromString,
                )


class ImagesServicer(object):
    """The greeting service definition.

    """

    def GetImages(self, request, context):
        """Sends a greeting
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetImageById(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def CreateImage(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def UpdateImage(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def DeleteImage(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ImagesServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'GetImages': grpc.unary_unary_rpc_method_handler(
                    servicer.GetImages,
                    request_deserializer=images__pb2.GetImagesRequest.FromString,
                    response_serializer=images__pb2.GetImagesResponse.SerializeToString,
            ),
            'GetImageById': grpc.unary_unary_rpc_method_handler(
                    servicer.GetImageById,
                    request_deserializer=images__pb2.GetImageByIdRequest.FromString,
                    response_serializer=images__pb2.GetImageByIdResponse.SerializeToString,
            ),
            'CreateImage': grpc.unary_unary_rpc_method_handler(
                    servicer.CreateImage,
                    request_deserializer=images__pb2.CreateImageRequest.FromString,
                    response_serializer=images__pb2.CreateImageResponse.SerializeToString,
            ),
            'UpdateImage': grpc.unary_unary_rpc_method_handler(
                    servicer.UpdateImage,
                    request_deserializer=images__pb2.UpdateImageRequest.FromString,
                    response_serializer=images__pb2.UpdateImageResponse.SerializeToString,
            ),
            'DeleteImage': grpc.unary_unary_rpc_method_handler(
                    servicer.DeleteImage,
                    request_deserializer=images__pb2.DeleteImageRequest.FromString,
                    response_serializer=images__pb2.DeleteImageResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'images.Images', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class Images(object):
    """The greeting service definition.

    """

    @staticmethod
    def GetImages(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/images.Images/GetImages',
            images__pb2.GetImagesRequest.SerializeToString,
            images__pb2.GetImagesResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetImageById(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/images.Images/GetImageById',
            images__pb2.GetImageByIdRequest.SerializeToString,
            images__pb2.GetImageByIdResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def CreateImage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/images.Images/CreateImage',
            images__pb2.CreateImageRequest.SerializeToString,
            images__pb2.CreateImageResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def UpdateImage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/images.Images/UpdateImage',
            images__pb2.UpdateImageRequest.SerializeToString,
            images__pb2.UpdateImageResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def DeleteImage(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/images.Images/DeleteImage',
            images__pb2.DeleteImageRequest.SerializeToString,
            images__pb2.DeleteImageResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
