from datetime import datetime

from engine.sternam_engine import SternamEngine
from battery.spindlerbattery import SpindlerBattery
from car import Car

class Glissade(Car):
	def __init__(self, warning_light_is_off, last_service_date, current_date):
		self.engine = SternamEngine(warning_light_is_off)
		self.battery = SpindlerBattery(last_service_date, current_date)

    def needs_service(self):
    	return self.engine.needs_service() or self.battery.needs_service()
