import unittest
from romano import a_numero

class RomanosTests(unittest.TestCase):
    def test_digitos_romanos(self):
        self.assertEqual(a_numero('I'), 1)
        self.assertEqual(a_numero('V'), 5)

    def test_numeros_completos(self):
        self.assertEqual(a_numero('XXV'), 25)
        self.assertEqual(a_numero('CDXXIV'), 424)  

    def test_no_se_resta_ni_V_L_D(self):
        with self.assertRaises(ValueError):
            a_numero('VC')

    def test_no_se_resta_mas_de_un_salto(self):
        self.assertEqual(a_numero('IV'), 4)
        self.assertEqual(a_numero('IX'), 9)
        with self.assertRaises(ValueError):
            a_numero('IL')

    def test_no_mas_de_tres_repeticiones(self):
        self.assertEqual(a_numero('III'))
        with self.assertRaises(ValueError):
            a_numero('IIII')        