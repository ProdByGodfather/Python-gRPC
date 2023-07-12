# Python & gRPC
Connecting gRPC to Python in a simple way and building a server and client to send and receive responses
<br>
## Implementation principles of the code
first you need go to `requirements.txt` and install libraries, for install with cmd:
```
pip install -r requirements.txt
```

# For Create Models on `protos/hello.proto` :

```proto
syntax = "proto3";

// The greeting service definition.
service Greeter {
  // Sends a greeting
  rpc SayHello (HelloRequest) returns (StringResponse) {}
}

message HelloRequest {
  string name = 1;
  int32 age = 2;
}

message StringResponse {
  string message = 1;
}
```

# For `server.py`:

1. import modules
```python
from concurrent import futures
import logging
import os
import grpc
from protos import hello_pb2, hello_pb2_grpc
```

<br>

2. for sent requests to clients

```python
class Greeter(hello_pb2_grpc.GreeterServicer):
    def SayHello(self, request, context):
        return hello_pb2.StringResponse(message=f'Hello, {request.name}! Your age is {request.age}')
```
3. for create server
   
```python
def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=4))
    hello_pb2_grpc.add_GreeterServicer_to_server(Greeter(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()
```

# for `client.py`:

1. Import modules
```python
import logging
import os
import grpc
from protos import hello_pb2, hello_pb2_grpc
```
2. for request to server ( It must already be running )
```python
def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = hello_pb2_grpc.GreeterStub(channel)
        response = stub.SayHello(hello_pb2.HelloRequest(name='Godfather', age=30))
        print("Greeter client received: " + response.message)

```
<br>

## The following code should be at the bottom of the file

```python
if __name__ == '__main__':
    logging.basicConfig()
    run()
```

