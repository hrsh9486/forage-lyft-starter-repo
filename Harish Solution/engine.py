from dataclasses import dataclass

@ dataclass
class Engine:
    def needs_service():
        pass


@ dataclass
class CapuletEngine(Engine):
    current_mileage: int
    last_service_mileage:int
    mileage_time: int = 30000
    
    def needs_service(self):
        if self.current_mileage-self.last_service_mileage>self.mileage_time:
            return True

@ dataclass
class WilloughbyEngine(Engine):
    current_mileage: int
    last_service_mileage:int
    mileage_time: int =60000
    
    def needs_service(self):
        if self.current_mileage-self.last_service_mileage>self.mileage_time:
            return True

@ dataclass
class SternmanEngine(Engine):
    warning_light_on: bool = False
    
    def needs_service(self):
        if self.warning_light_on:
            return True
