invalid_message = "Invalid temperature"

# check validity first - then do conversion?
def convert_temperature(temperature, unit):

    if unit == "K":
        celsius = temperature - 273.15
        farenheit = celsius_to_farenheit(celsius)
        return celsius_check(celsius), farenheit_check(farenheit)

    elif unit == "C":
        kelvin = temperature + 273.15
        farenheit = celsius_to_farenheit(temperature)
        return farenheit_check(farenheit), kelvin_check(kelvin)

    elif unit == "F":
        celsius = farenheit_to_celsius(temperature)
        if type(celsius) == str:
            kelvin = invalid_message
        else:
            kelvin = celsius + 273.15
        return celsius_check(celsius), kelvin_check(kelvin)

    else:
        return "Invalid Unit"

def kelvin_check(kelvin):
    """"Checks to ensure that Kelvin isn't negative"""
    if type(kelvin) == str or kelvin < 0:
        return invalid_message
    else:
        return kelvin

def celsius_check(celsius):
    """"Checks to ensure that Celsius isn't below 273.15"""
    if  celsius < -273.15:
        return invalid_message
    else:
        return celsius

def farenheit_check(fahrenheit):
    """"Checks to ensure that Fahrenheit isn't below -459.67"""
    if fahrenheit < -459.67:
        return invalid_message
    else:
        return fahrenheit
def farenheit_to_celsius(temperature):
    """""Coverts celsius to Farenheit"""
    celsius = (temperature - 32) * (5 / 9)
    return celsius_check(celsius)

def celsius_to_farenheit(temperature):
    """""Coverts Farenheit to celsius"""
    fahrenheit = (temperature * (9 / 5)) + 32
    return farenheit_check(fahrenheit)


# while True:
#     temperature = float(input("Temp"))
#     unit = str(input("unit"))
#     print(convert_temperature(temperature, unit))

# attempt 2


class ConvertTemperature():

    def __init__(self, temperature, unit):
        self.temperature = temperature
        self.unit = unit

    def out(self):
        if self.unit == "F":
            self.fahrenheit = self.temperature
            self.farenheit_check()
            self.farenheit_to_celsius()
            self.kelvin = self.celsius + 273.15
            return self.celsius, self.kelvin
        elif self.unit == "C":
            self.celsius = self.temperature
            self.kelvin = self.temperature + 273.15
            self.celsius_check()
            self.celsius_to_farenheit()
            return self.fahrenheit, self.kelvin
        elif self.unit == "K":
            self.celsius = self.temperature - 273.15
            self.kelvin = self.temperature
            self.kelvin_check()
            self.celsius_to_farenheit()
            return self.fahrenheit, self.kelvin
        else:
            return "Invalid Unit"

    def celsius_to_farenheit(self):
        """""Coverts Farenheit to celsius"""
        fahrenheit = (self.temperature * (9 / 5)) + 32
        self.fahrenheit = fahrenheit

    def farenheit_to_celsius(self):
        """""Coverts celsius to Farenheit"""
        celsius = (self.temperature - 32) * (5 / 9)
        self.celsius = celsius

    def farenheit_check(self):
        """"Checks to ensure that Fahrenheit isn't below -459.67"""
        if self.fahrenheit < -459.67:
            raise UserWarning("Invalid Temperature")

    def kelvin_check(self):
        """"Checks to ensure that Kelvin isn't negative"""
        if self.kelvin < 0:
            raise UserWarning("Invalid Temperature")

    def celsius_check(self):
        """"Checks to ensure that Celsius isn't below 273.15"""
        if self.celsius < -273.15:
            raise UserWarning("Invalid Temperature")

while True:
    temperature = float(input("Temp"))
    unit = str(input("unit"))
    print(ConvertTemperature(temperature, unit).out())




# """"
# # initial code
# ```python=
# def convert_temperature(temperature, unit):
#     if unit == "F":
#         # Convert Fahrenheit to Celsius
#         celsius = (temperature - 32) * (5 / 9)
#         if celsius < -273.15:
#             # Invalid temperature, below absolute zero
#             return "Invalid temperature"
#         else:
#             # Convert Celsius to Kelvin
#             kelvin = celsius + 273.15
#             if kelvin < 0:
#                 # Invalid temperature, below absolute zero
#                 return "Invalid temperature"
#             else:
#                 fahrenheit = (celsius * (9 / 5)) + 32
#                 if fahrenheit < -459.67:
#                     # Invalid temperature, below absolute zero
#                     return "Invalid temperature"
#                 else:
#                     return celsius, kelvin
#     elif unit == "C":
#         # Convert Celsius to Fahrenheit
#         fahrenheit = (temperature * (9 / 5)) + 32
#         if fahrenheit < -459.67:
#             # Invalid temperature, below absolute zero
#             return "Invalid temperature"
#         else:
#             # Convert Celsius to Kelvin
#             kelvin = temperature + 273.15
#             if kelvin < 0:
#                 # Invalid temperature, below absolute zero
#                 return "Invalid temperature"
#             else:
#                 return fahrenheit, kelvin
#     elif unit == "K":
#         # Convert Kelvin to Celsius
#         celsius = temperature - 273.15
#         if celsius < -273.15:
#             # Invalid temperature, below absolute zero
#             return "Invalid temperature"
#         else:
#             # Convert Celsius to Fahrenheit
#             fahrenheit = (celsius * (9 / 5)) + 32
#             if fahrenheit < -459.67:
#                 # Invalid temperature, below absolute zero
#                 return "Invalid temperature"
#             else:
#                 return celsius, fahrenheit
#     else:
#         return "Invalid unit"
# ```
# """"