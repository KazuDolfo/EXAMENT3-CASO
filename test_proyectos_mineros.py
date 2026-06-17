# PRUEBAS UNITARIAS - SISTEMA MINERO
import unittest
from proyectos_mineros import ProyectoMinero, CarteraInversion, ValidationError

class TestCartera(unittest.TestCase):
    def test_monto_cero(self):
        p = ProyectoMinero("Test", 0)
        self.assertEqual(p.inversion_millones, 0)

    def test_error_negativo(self):
        with self.assertRaises(ValidationError):
            ProyectoMinero("Error", -1)

    def test_auditoria(self):
        p = ProyectoMinero("Coroccohuayco", 590)
        p.actualizar_monto(1500, "Ampliacion")
        self.assertEqual(len(p.historial_cambios), 2)

    def test_caso_real(self):
        total_2023 = 53130
        cartera = CarteraInversion(2024)
        cartera.agregar_proyecto(ProyectoMinero("Total", 54556))
        diff, porc = cartera.comparar_con_anterior(total_2023)
        self.assertEqual(diff, 1426)

if __name__ == "__main__":
    unittest.main()
