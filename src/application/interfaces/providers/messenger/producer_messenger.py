from abc import ABC, abstractmethod


class ProducerMessenger(ABC):
    """Messenger Queue Producer Interface"""

    @abstractmethod
    def produce(self, to: str, data: dict):
        """Produce an message to destination"""
        raise NotImplementedError()
