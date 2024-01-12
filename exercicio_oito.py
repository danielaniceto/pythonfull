"""Esse programa tem por função, receber uma temperatura em farenheit e
converte-la para celsius, apresentando para o user posteriormente"""

def is_temperature_validation(temperature):
    if not isinstance(temperature, (float, int)):
        raise Exception ("It's a not valid temperature!!!\n")
    
    else:
        return "It's OK, your temperature is valid!!!\n"

def is_converte_temperature(temperature):

    convert_temperature =  (temperature-32) * 5/9
    
    return f"{convert_temperature:.2f}º"

def main():
    temperature = float(input("Enter a temperature in farenheit here for covert in celsius: "))

    validation_temperature = is_temperature_validation(temperature)
    print(validation_temperature)

    convert_temperature = is_converte_temperature(temperature)
    print(convert_temperature)

main()
