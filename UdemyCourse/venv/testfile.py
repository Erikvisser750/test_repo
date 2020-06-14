import unittest
import main

class TestMain(unittest.TestCase):
    def test_multiply(self):
        test_param = 'asd'
        result = main.multiply2(test_param)
        self.assertIsInstance(result, ValueError)

unittest.main()




