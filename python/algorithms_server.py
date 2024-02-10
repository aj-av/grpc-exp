from concurrent import futures

import grpc
import algorithms_pb2
from algorithms_pb2_grpc import AlgoServiceServicer
from algorithms_pb2_grpc import add_AlgoServiceServicer_to_server

class AlgoServiceServer(AlgoServiceServicer):
    def AddNums(self, request, context):
        return algorithms_pb2.AddNumsResponse(sum=request.num1+request.num2)
    
    def ReverseString(self, request, context):
        return algorithms_pb2.ReverseStringResponse(reversed_str=request.str[::-1])
    
    def FindMax(self, request, context):
        return algorithms_pb2.FindMaxResponse(max=max(request.nums))
    

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
    add_AlgoServiceServicer_to_server(AlgoServiceServer(), server)
    server.add_insecure_port('[::]:50051')
    try:
        server.start()
        print("Server started at port 50051")
        server.wait_for_termination()
    except Exception as e:
        print("Error: ", e)
        server.stop(0)

if __name__=='__main__': 
    serve()
