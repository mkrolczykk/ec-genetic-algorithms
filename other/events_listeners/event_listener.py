from abc import ABC, abstractmethod


class EventListener(ABC):
    @abstractmethod
    def listen(self):
        pass
