
from context import context
class ExampleApplication():
	main():
		contex = Contex()

		cartype = getCarTypeInput()
		current_mileage=getMileageInput()
		last_service_mileage = getServiceMileage()
		last_service_date  =getServiceDate()
		current_date = getDateInput()
		warning_light_is_off = getLightInput()
		if(cartype=="Calliope"):
			context.setCar(Calliope(current_mileage, last_service_mileage, last_service_date, current_date))
		if(cartype == "Glissade"):
			context.setCar(Glissade(current_mileage, last_service_mileage, last_service_date, current_date))
		if(cartype == "Palindrome"):
			context.setCar(Palindrome(warning_light_is_off, last_service_date, current_date))
		if(cartype == "Rorschach"):
			context.setCar(Rorschach(current_mileage, last_service_mileage, last_service_date, current_date))
		if(cartype == "Thovex"):
			context.setCar(Thovex(current_mileage, last_service_mileage, last_service_date, current_date))

		result = context.determin_service_need()

		return result

