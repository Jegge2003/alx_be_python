class Calculator:
    #Class attribute initialization
    calculation_type = "Arithmetic Operations"
    
    #A static method returning the sum of two number a and b
    @staticmethod
    def add (a, b):
        return a + b
    
    #A class method returning the product of two numbers a and b
    @classmethod
    def multiply(cls, a, b):
        print(f"Calculation type: {cls.calculation_type}")
        return a*b
