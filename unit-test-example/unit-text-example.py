# Andrés López Esquivel
# Wednesday, July 7, 2021
# Unit test example

import unittest


def sum(num1, num2):
    return num1 + num2


class CodeTest(unittest.TestCase):
    
    def test_sum_function(self):
        num1 = 1
        num2 = 2
        result = sum(num1, num2)
        self.assertEqual(result, num1 + num2)

if __name__ == "__main__":
    unittest.main()