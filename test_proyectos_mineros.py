import unittest
from proyectos_mineros import ProyectoMinero, CarteraInversion, ValidationError

class TestCarteraQA(unittest.TestCase):
    
    def setUp(self):
        self.cartera = CarteraInversion(2024)

    def test_boundary_monto_cero(self):
        """QA-01: Validar que se permite inversión de cero (valor límite)."""
        p = ProyectoMinero("Proyecto Test", 0)
        self.assertEqual(p.inversion_millones, 0)

    def test_error_monto_negativo(self):
        """QA-02: Validar que montos negativos lanzan ValidationError."""
        with self.assertRaises(ValidationError):
            ProyectoMinero("Error Negativo", -1)

    def test_error_nombre_corto(self):
        """QA-03: Validar longitud mínima del nombre."""
        with self.assertRaises(ValidationError):
            ProyectoMinero("Ab", 100)

    def test_historial_auditoria(self):
        """QA-04: Verificar que el historial de cambios registra movimientos."""
        p = ProyectoMinero("Coroccohuayco", 590)
        p.actualizar_monto(1500, "Ampliación de infraestructura")
        
        self.assertEqual(len(p.historial_cambios), 2)
        self.assertEqual(p.historial_cambios[0][0], 590)
        self.assertEqual(p.inversion_millones, 1500)

    def test_comparacion_exacta_caso(self):
        """QA-05: Validar los datos específicos del CASO.txt."""
        total_2023 = 53130
        # Simulamos llegada al total 2024
        self.cartera.agregar_proyecto(ProyectoMinero("Total Consolidado", 54556))
        
        diff, porc = self.cartera.comparar_con_anterior(total_2023)
        self.assertEqual(diff, 1426)
        self.assertAlmostEqual(porc, 2.684, places=2)

if __name__ == '__main__':
    unittest.main()
