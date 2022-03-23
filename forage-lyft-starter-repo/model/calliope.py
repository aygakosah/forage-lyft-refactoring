from datetime import datetime

from engine.capulet_engine import CapuletEngine
from battery.spindlerbattery import SpindlerBattery
from car import Car


class Calliope(Car):
	def __init__(self, current_mileage, last_service_mileage, last_service_date, current_date):
		self.engine = CapuletEngine(current_mileage, last_service_mileage)
		self.battery = SpindlerBattery(last_service_date, current_date)

    def needs_service(self):
    	return self.engine.needs_service() or self.battery.needs_service()
        
