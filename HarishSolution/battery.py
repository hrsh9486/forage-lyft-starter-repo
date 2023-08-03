from dataclasses import dataclass
from datetime import datetime,date
from utils import add_years_to_date

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
    def needs_service(self):
        date_which_battery_should_be_serviced_by = add_years_to_date(self.last_service_date, 2)
        if date_which_battery_should_be_serviced_by < self.current_date:
            return True
        else:
            return False


@dataclass
class NubbinBattery(Battery):
    
    def needs_service(self):
        date_which_battery_should_be_serviced_by = add_years_to_date(self.last_service_date, 4)
        if date_which_battery_should_be_serviced_by < self.current_date:
            return True
        else:
            return False

