def perform_operation(num1, num2, operation):
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide' and num2 == 0:
        return "You cannot divide by 0"
    elif operation == 'divide' and num2 != 0:
        return num1 / num2
