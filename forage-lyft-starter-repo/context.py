from car import Car


class Context():
	def __init__(self):
		self.car = Car()

	def setCar(self, particular_model):
		self.car = particular_model

	def determine_service_need():
		return self.car.needs_service()
