from abc import ABC, abstractmethod
from engine import Engine
from battery import Battery

class Car(ABC):
    def __init__(self, engine, battery):
        self.engine = Engine()
        self.battery = Battery()

    @abstractmethod
    def needs_service(self):
        pass
