# Import modules

import logging
import os
import grpc
from protos import hello_pb2, hello_pb2_grpc

'''
    Before Run clinet.py on localhost:50051 Go to server.py and run it
    *________________________________________________________________*
    
    The client file basically sends a request to the server 
    finally displays the response received from the server.py side.
'''

def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = hello_pb2_grpc.GreeterStub(channel)
        response = stub.SayHello(hello_pb2.HelloRequest(name='Godfather', age=30))
        print("Greeter client received: " + response.message)
        
        
# The following code should be at the bottom of the file
if __name__ == '__main__':
    logging.basicConfig()
    run()