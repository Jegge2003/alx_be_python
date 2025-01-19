import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    #Unit test for the SimpleCalculator class.

    def setUp(self):
        #Set up the SimpleCalculator instance before each test.
        self.calc = SimpleCalculator()

    def test_addition(self):
        #Test the add method
        self.assertEqual(self.calc.add(2,3), 5) #Basic addition
        self.assertEqual(self.calc.add(-1,1), 0) #Addition with negative numbers
        self.assertEqual(self.calc.add(0,0), 0) #Zero addition
        self.assertEqual(self.calc.add(1.5,2.5), 4.0) #Float addition

    def test_subtraction(self):
        #Test the subtract method.
        self.assertEqual(self.calc.subtract(5,3), 2) #Basic substraction
        self.assertEqual(self.calc.subtract(-1,-1), 0) #Subtraction with negatives
        self.assertEqual(self.calc.subtract(0,5), -5) #Negative result
        self.assertEqual(self.calc.subtract(2.5,1.5), 1.0) #Float subtraction

    def test_multiplication(self):
        #Test the multiply method
        self.assertEqual(self.calc.multiply(2,3), 6) #Basic multiplication
        self.assertEqual(self.calc.multiply(-1,1), -1) #Multiplication with a negative number
        self.assertEqual(self.calc.multiply(0,5), 0) #Multiplication with zero
        self.assertEqual(self.calc.multiply(1.5, 2), 3.0) #Float multiplication

    def test_division(self):
        #Test the divide method
        self.assertEqual(self.calc.divide(6,3), 2.0) #Basic division operation
        self.assertEqual(self.calc.divide(-6,2), -3.0) #Division with a negative number
        self.assertEqual(self.calc.divide(5,2), 2.5) #Float result
        self.assertIsNone(self.calc.divide(5,0)) #Division by zero

    def test_edge_cases(self):
        #Test edge cases for all operations
        self.assertEqual(self.calc.add(float('inf'), 1), float('inf')) #Adding infinity
        self.assertEqual(self.calc.multiply(float('inf'), 0), 0) #Zero multiplied by infinity
        self.assertIsNone(self.calc.divide(1, float('inf'))) #Division by infinity

#Run the tests
if __name__ == '__main__':
    unittest.main()
