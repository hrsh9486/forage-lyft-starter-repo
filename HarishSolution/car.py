from dataclasses import dataclass
from engine import Engine
from battery import Battery


@ dataclass
class Car:
    engine: Engine
    battery: Battery

    def needs_service(self):
        return self.engine.needs_service() or self.battery.needs_service()