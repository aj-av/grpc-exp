import grpc
from exchange_pb2 import HelloRequest
from exchange_pb2_grpc import HandshakeStub

def main():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = HandshakeStub(channel)
        req = HelloRequest(request='Ajay')
        print(f"Sent\n {req}")
        response = stub.Hello(req)
        print(f"Recieved\n {response}")

if __name__=='__main__':
    main()