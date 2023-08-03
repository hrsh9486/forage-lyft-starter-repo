from dataclasses import dataclass
from engine import Engine
from battery import Battery


@ dataclass
class Car:
    engine: Engine
    battery: Battery
