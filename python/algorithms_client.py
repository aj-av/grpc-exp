import grpc
import algorithms_pb2
from algorithms_pb2_grpc import AlgoServiceStub

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = AlgoServiceStub(channel)
        # AddNums
        print("Adding numbers")
        response = stub.AddNums(algorithms_pb2.AddNumsRequest(num1=5, num2=3))
        print("Sum: ", response.sum)

        # ReverseString
        print("Reversing string")
        response = stub.ReverseString(algorithms_pb2.ReverseStringRequest(str="hello"))
        print("Reversed string: ", response.reversed_str)

        # FindMax
        print("Finding max")
        response = stub.FindMax(algorithms_pb2.FindMaxRequest(nums=[1, 5, 3, 6, 2]))
        print("Max: ", response.max)

if __name__ == '__main__':
    run()