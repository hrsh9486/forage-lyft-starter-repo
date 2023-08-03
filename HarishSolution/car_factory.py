from dataclasses import dataclass
from datetime import datetime, date
from car import Car
import engine
import battery

@dataclass
class CarFactory:
    def create_calliope(current_date:date,last_service_date:date,current_mileage:int,last_service_mileage:int):
        calliope=Car(engine.CapuletEngine(last_service_mileage,current_mileage),battery.SpindlerBattery(last_service_date,current_date))
        return calliope

    def create_glissade(current_date:date,last_service_date:date,current_mileage:int,last_service_mileage:int):
        glissade=Car(engine.WilloughbyEngine(last_service_mileage,current_mileage),battery.SpindlerBattery(last_service_date,current_date))
        return glissade
    
    def create_palindrome(current_date:date,last_service_date:date,warning_light_is_on:bool = False):
        palindrome=Car(engine.SternmanEngine(warning_light_is_on),battery.SpindlerBattery(last_service_date,current_date))
        return palindrome
    
    def create_rorschach(current_date:date,last_service_date:date,current_mileage:int,last_service_mileage:int):
        rorschach=Car(engine.WilloughbyEngine(last_service_mileage,current_mileage),battery.NubbinBattery(last_service_date,current_date))
        return rorschach
    
    def create_thovex(current_date:date,last_service_date:date,current_mileage:int,last_service_mileage:int):
        thovex=Car(engine.CapuletEngine(last_service_mileage,current_mileage),battery.NubbinBattery(last_service_date,current_date))
        return thovex

    
