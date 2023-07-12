
# Import modules

from concurrent import futures
import logging
import os
import grpc
from protos import hello_pb2, hello_pb2_grpc

'''
    after Run it on localhost:50051, run client.py 
    *____________________________________________*
    
    the server file basically create local server and connect to models on protos/hello.proto
    Two Python files inside the protos folder were created automatically with the following command:
    
    python -m grpc_tools.protoc -I=. --python_out=. --grpc_python_out=. ./protos/hello.proto 
'''

# For Sent Requests to Client
class Greeter(hello_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        return hello_pb2.StringResponse(message=f'Hello, {request.name}! Your age is {request.age}')


# For Create Server
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=4))
    hello_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()


# The following code should be at the bottom of the file
if __name__ == '__main__':
    logging.basicConfig()
    serve()