import unittest
from romano import RomanNumber

class RomanNumberClassTests(unittest.TestCase):
    def test_crear_Numero_romano(self):
        uno = RomanNumber(1)
        self.assertEqual(uno.valor, 1)
        self.assertEqual(uno.cadena, 'I')

        with self.assertRaises(ValueError):
            cuatromil = RomanNumber(4000)

    def test_metodos_magicos_representacion(self):
        uno = RomanNumber(1)

        self.assertEqual(uno.cadena, "I")        