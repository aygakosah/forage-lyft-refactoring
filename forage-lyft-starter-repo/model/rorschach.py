from datetime import datetime
from car import Car
from engine.willoughby_engine import WilloughbyEngine
from battery.nubbin import Nubbin


class Rorschach(Car):
	def __init__(self, current_mileage, last_service_mileage, last_service_date, current_date):
		self.engine = WilloughbyEngine(current_mileage, last_service_mileage)
		self.battery = NubbinBattery(last_service_date, current_date)

    def needs_service(self):
        return engine.needs_service() or battery.needs_service()