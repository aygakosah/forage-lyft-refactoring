from datetime import datetime

from engine.willoughby_engine import WilloughbyEngine
from battery.spindlerbattery import SpindlerBattery

class Glissade(Car):
	def __init__(self, current_mileage, last_service_mileage, last_service_date, current_date):
		self.engine = WilloughbyEngine(current_mileage, last_service_mileage)
		self.battery = SpindlerBattery(last_service_date, current_date)

    def needs_service(self):
    	return self.engine.needs_service() or self.battery.needs_service()
