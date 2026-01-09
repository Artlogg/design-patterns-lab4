from abc import ABC, abstractmethod


class Logger(ABC):
    @abstractmethod
    def log(self, message: str):
        pass


class ExternalLogger:
    def log_message(self, msg: str):
        print(f"External log: {msg}")


class LoggerAdapter(Logger):
    def __init__(self, external_logger: ExternalLogger):
        self._external_logger = external_logger

    def log(self, message: str):
        self._external_logger.log_message(message)


if __name__ == "__main__":
    external_logger = ExternalLogger()
    logger = LoggerAdapter(external_logger)

    logger.log("This is a test message")
