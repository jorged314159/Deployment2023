from Calculadora import Calculadora
import unittest

class TestCalculadora(unittest.TestCase):

    def test_suma_2_mas_2(self):
        calc = Calculadora()
        self.assertEqual(4, calc.suma(2, 2))

if __name__ == '__main__':
    unittest.main()

