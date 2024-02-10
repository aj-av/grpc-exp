from concurrent import futures

import grpc
from exchange_pb2_grpc import add_HandshakeServicer_to_server
from exchange_pb2_grpc import HandshakeServicer
from exchange_pb2 import HelloResponse

class HandshakeService(HandshakeServicer):
    def Hello(self, request, context):
        print("Request from client: ", request)
        return HelloResponse(response="Recieved Hello! Hi")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
    add_HandshakeServicer_to_server(HandshakeService(), server)
    server.add_insecure_port('[::]:50051')
    try:
        server.start()
        print("Server started at port 50051")
        server.wait_for_termination()
    except Exception as e:
        print("Error: ", e)
        server.stop(0)

if __name__ == '__main__':
    serve()