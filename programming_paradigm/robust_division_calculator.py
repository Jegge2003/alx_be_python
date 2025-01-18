def safe_divide(numerator, denominator):
    try:
        #Converting values to floats
        numerator = float(numerator)
        denominator = float(denominator)

        #Performing division operation
        result = numerator / denominator

        #Returning the output
        return f'The result of the division is {result:.1f}'

    
    except ZeroDivisionError:
        return f'Error: Cannot divide by zero.'

    except ValueError:
        return f'Error: Please enter numeric values only'
