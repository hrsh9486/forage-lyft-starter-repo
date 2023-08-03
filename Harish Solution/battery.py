from dataclasses import dataclass
from datetime import datetime,date

@dataclass
class Battery:
    last_service_date: date
    current_date: date
    service_time: int
    
    def needs_service(self):
        if self.current_date - self.last_service_date > self.service_time:
            return True


@dataclass
class SpindlerBattery(Battery):
    service_time = 2

@dataclass
class NubbinBattery(Battery):
    service_time = 4

