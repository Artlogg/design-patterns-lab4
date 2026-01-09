from abc import ABC, abstractmethod


# Implementor
class Device(ABC):
    @abstractmethod
    def print(self, data: str):
        pass


class Monitor(Device):
    def print(self, data: str):
        print(f"Displaying on monitor: {data}")


class Printer(Device):
    def print(self, data: str):
        print(f"Printing to paper: {data}")


# Abstraction
class Output(ABC):
    def __init__(self, device: Device):
        self._device = device

    @abstractmethod
    def render(self, data: str):
        pass


# Refined Abstractions
class TextOutput(Output):
    def render(self, data: str):
        self._device.print(f"Text: {data}")


class ImageOutput(Output):
    def render(self, data: str):
        self._device.print(f"Image: [Binary data: {data}]")


if __name__ == "__main__":
    monitor = Monitor()
    printer = Printer()

    text_on_monitor = TextOutput(monitor)
    text_on_printer = TextOutput(printer)

    text_on_monitor.render("Hello, world!")
    text_on_printer.render("Hello, world!")

    image_on_monitor = ImageOutput(monitor)
    image_on_monitor.render("101010101")
