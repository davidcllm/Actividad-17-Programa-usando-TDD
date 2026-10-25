import unittest
from main import calcular_nomina

# pruebas diseñadas antes de programar la función.
class TestCalcularNomina(unittest.TestCase):

    # pruebas con valores no válidos
    def test_horas_negativas(self):
        """No se permiten horas menores a 0"""
        self.assertEqual(calcular_nomina(-5), "número no válido")
        
    def test_horas_excesivas(self):
        """No se permiten horas mayores a 64"""
        self.assertEqual(calcular_nomina(65), "número no válido")
        
    def test_tipo_de_dato_incorrecto(self):
        """No se permiten letras o caracteres especiales"""
        self.assertEqual(calcular_nomina("cuarenta"), "número no válido")
        self.assertEqual(calcular_nomina(None), "número no válido")

    # pruebas con valores válidos
    def test_cero_horas(self):
        """Límite inferior válido (0 horas)"""
        self.assertEqual(calcular_nomina(0), 0)
        
    def test_pago_normal(self):
        """De 1 a 40 horas (200 x hora)"""
        self.assertEqual(calcular_nomina(20), 4000)
        self.assertEqual(calcular_nomina(40), 8000) # Límite de pago normal
        
    def test_pago_horas_dobles(self):
        """De 41 a 56 horas (40 normales + excedentes al doble)"""
        # 41 hrs = (40 * 200) + (1 * 400) = 8400
        self.assertEqual(calcular_nomina(41), 8400)
        
        # 56 hrs = (40 * 200) + (16 * 400) = 8000 + 6400 = 14400
        self.assertEqual(calcular_nomina(56), 14400) # Límite de pago doble
        
    def test_pago_horas_triples(self):
        """De 57 a 64 horas (40 norm + 16 dobles + excedentes al triple)"""
        # 57 hrs = 8000 + 6400 + (1 * 600) = 15000
        self.assertEqual(calcular_nomina(57), 15000)
        
        # 64 hrs = 8000 + 6400 + (8 * 600) = 19200
        self.assertEqual(calcular_nomina(64), 19200) # Límite máximo del sistema

    def test_horas_con_decimales(self):
        """El sistema debe soportar fracciones de hora (ej. 30.5 horas)"""
        # 30.5 * 200 = 6100
        self.assertEqual(calcular_nomina(30.5), 6100.0)

if __name__ == '__main__':
    unittest.main(verbosity=2)