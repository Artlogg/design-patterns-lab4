from abc import ABC, abstractmethod
from enum import Enum


class RequestType(Enum):
    TYPE_A = 1
    TYPE_B = 2


class Request:
    def __init__(self, request_type):
        self.type = request_type


class Handler(ABC):
    def __init__(self):
        self._next_handler = None

    def set_next(self, handler):
        self._next_handler = handler
        return handler

    @abstractmethod
    def handle(self, request):
        pass


class HandlerA(Handler):
    def handle(self, request):
        if request.type == RequestType.TYPE_A:
            print("HandlerA handled the request")
        elif self._next_handler:
            self._next_handler.handle(request)


class HandlerB(Handler):
    def handle(self, request):
        if request.type == RequestType.TYPE_B:
            print("HandlerB handled the request")
        elif self._next_handler:
            self._next_handler.handle(request)


if __name__ == "__main__":
    handler_a = HandlerA()
    handler_b = HandlerB()

    handler_a.set_next(handler_b)

    handler_a.handle(Request(RequestType.TYPE_A))
    handler_a.handle(Request(RequestType.TYPE_B))
