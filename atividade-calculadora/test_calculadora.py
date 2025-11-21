import unittest
from calculadora import somarNum, subtrairNum, multiplicarNum, dividirNum

class TestCalculadora(unittest.TestCase):

    def test_soma(self):
        self.assertEqual(somarNum(10, 5), 15)
        self.assertEqual(somarNum(-3, 7), 4)

    def test_subtracao(self):
        self.assertEqual(subtrairNum(10, 4), 6)
        self.assertEqual(subtrairNum(3, 9), -6)

    def test_multiplicacao(self):
        self.assertEqual(multiplicarNum(7, 6), 42)
        self.assertEqual(multiplicarNum(15, 0), 0)

    def test_divisao(self):
        self.assertEqual(dividirNum(20, 4), 5)
        # divisão por zero deve retornar None
        self.assertIsNone(dividirNum(10, 0))

if __name__ == "__main__":
    unittest.main()
