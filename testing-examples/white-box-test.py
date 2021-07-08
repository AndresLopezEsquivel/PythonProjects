# Andrés López Esquivel
# Wednesday, July 7, 2021
# White box test example

import unittest

def is_an_adult(age):
    if age >= 18:
        return True
    else:
        return False

class WhiteBoxTest(unittest.TestCase):
    
    def test_is_adult_func(self):
        age = 20
        result = is_an_adult(age=age)
        self.assertEqual(result, age >= 18)

if __name__ == "__main__":
    unittest.main()