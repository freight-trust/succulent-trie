# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import cztrie_pb2 as cztrie__pb2


class CztrieServiceStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Get = channel.unary_unary(
        '/CztrieService/Get',
        request_serializer=cztrie__pb2.GetRequest.SerializeToString,
        response_deserializer=cztrie__pb2.GetResponse.FromString,
        )
    self.Put = channel.unary_unary(
        '/CztrieService/Put',
        request_serializer=cztrie__pb2.PutRequest.SerializeToString,
        response_deserializer=cztrie__pb2.PutResponse.FromString,
        )
    self.Del = channel.unary_unary(
        '/CztrieService/Del',
        request_serializer=cztrie__pb2.DeleteRequest.SerializeToString,
        response_deserializer=cztrie__pb2.DeleteResponse.FromString,
        )
    self.Create = channel.unary_unary(
        '/CztrieService/Create',
        request_serializer=cztrie__pb2.DatasetRequest.SerializeToString,
        response_deserializer=cztrie__pb2.DatasetResponse.FromString,
        )


class CztrieServiceServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def Get(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Put(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Del(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def Create(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_CztrieServiceServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Get': grpc.unary_unary_rpc_method_handler(
          servicer.Get,
          request_deserializer=cztrie__pb2.GetRequest.FromString,
          response_serializer=cztrie__pb2.GetResponse.SerializeToString,
      ),
      'Put': grpc.unary_unary_rpc_method_handler(
          servicer.Put,
          request_deserializer=cztrie__pb2.PutRequest.FromString,
          response_serializer=cztrie__pb2.PutResponse.SerializeToString,
      ),
      'Del': grpc.unary_unary_rpc_method_handler(
          servicer.Del,
          request_deserializer=cztrie__pb2.DeleteRequest.FromString,
          response_serializer=cztrie__pb2.DeleteResponse.SerializeToString,
      ),
      'Create': grpc.unary_unary_rpc_method_handler(
          servicer.Create,
          request_deserializer=cztrie__pb2.DatasetRequest.FromString,
          response_serializer=cztrie__pb2.DatasetResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'CztrieService', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
