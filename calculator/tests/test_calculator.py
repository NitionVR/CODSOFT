import unittest
from test_base import captured_io
from io import StringIO
import calculator

class MyTestCase(unittest.TestCase):
    
    def test_add_integers(self):
        result = calculator.add(10,10)
        self.assertEqual(result,20)

    def test_add_floats(self):
        result = calculator.add(10.225,10.225)
        self.assertEqual(result,20.45)

    def test_multiply_integers(self):
        result = calculator.multiply(5,5)
        self.assertEqual(result,25)

    def test_multiply_floats(self):
        result = calculator.multiply(2.5,2.5)
        self.assertEqual(result,6.25)

    def test_divide_integers(self):
        result = calculator.divide(25,5)
        self.assertEqual(result,5)

    def test_divide_floats(self):
        result = calculator.divide(5,2)
        self.assertEqual(result,2.5)

    def test_get_numbers_input_correct(self):
        with captured_io(StringIO("1\n2\n")) as (out,err):
            number_1,number_2 = calculator.get_numbers_input()
        self.assertEqual((number_1,number_2),(1,2))
    
    def test_get_numbers_input_invalid(self):
        with captured_io(StringIO("1\n'a'\n2\n2\n")) as (out,err):
            number_1,number_2 = calculator.get_numbers_input()
        output = out.getvalue().strip()
        expected_output = "Enter the first number: \nEnter the second number: \nIncorrect input. Try again.\
\nEnter the first number: \nEnter the second number: "
        self.assertEqual(output,expected_output)

    def test_get_operation(self):
        with captured_io(StringIO("+\n")) as (out,err):
            result = calculator.get_operation()
        self.assertEqual(result,"+")

        with captured_io(StringIO("-\n")) as (out,err):
            result = calculator.get_operation()
        self.assertEqual(result,"-")

        with captured_io(StringIO("/\n")) as (out,err):
            result = calculator.get_operation()
        self.assertEqual(result,"/")

        with captured_io(StringIO("*\n")) as (out,err):
            result = calculator.get_operation()
        self.assertEqual(result,"*")
        
if __name__ == "__main__":
    unittest.main()