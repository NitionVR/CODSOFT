import unittest
from test_base import captured_io
from io import StringIO
import todoApp

class MyTestCase(unittest.TestCase):

    def test_show_tasks(self):
        with captured_io(StringIO()) as (out,err):
            tasks = {1:"Build a to-do application", 2: "Turn it into an API"}
            todoApp.show_tasks(tasks)
        output = out.getvalue().strip()
        self.assertEqual(output,"Tasks: \n1. Build a to-do application\n2. Turn it into an API")

    def test_key_gen(self):
        todoApp.random.randint = lambda a, b : 1
        output = todoApp.key_gen(set())
        self.assertEqual(output,1)
        
        output = todoApp.key_gen({1,2,3})
        self.assertEqual(output,4)

if __name__ == "__main__":
    unittest.main()