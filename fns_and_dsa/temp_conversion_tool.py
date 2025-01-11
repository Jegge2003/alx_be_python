#Defining the global conversion factors
FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

#Function to convert Fahrenheit to Celsius
def convert_to_celsius(Fahrenheit):
    return (Fahrenheit - 32 ) * FAHRENHEIT_TO_CELSIUS_FACTOR

#Function to convert Celsius to Fahrenheit
def convert_to_fahrenheit(Celsius):
    return (Celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

#Main script logic
def main():

    #Prompt user to input temperature value
    temp = float(input('Enter the temperature to convert: '))

    #Prompt user to choose either Celsius or Fahrenheit 
    unit  = input('Is this temperature in Celsius or Fahrenheit? (C/F): ')
    
    #Changing from celsius to fahrenheit
    if temp.isdigit() and unit == 'C':
        fahrenheit = convert_to_fahrenheit(temp)
        print(f'{temp}°C is {fahrenheit}°F')

    #Changing from fahrenheit to celsius
    elif temp.isdigit() and unit == 'F':
        celsius = convert_to_celsius(temp)
        print(f'{temp}°F is {celsius}°C')
    
    else: #Checking wrong inputs
        print('Invalid temperature. Please enter a numeric value.')

#To execute directly and not as a script
if __name__ == '__main__':
    main()
