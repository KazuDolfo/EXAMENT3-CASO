import unittest
from proyectos_mineros import ProyectoMinero, CarteraInversion

class TestCarteraInversion(unittest.TestCase):
    def test_calcular_total_inversion(self):
        cartera = CarteraInversion(2024)
        cartera.agregar_proyecto(ProyectoMinero("Reposición Ferrobamba", 1753))
        cartera.agregar_proyecto(ProyectoMinero("Coimolache Sulfuros", 598))
        
        self.assertEqual(cartera.calcular_total_inversion(), 1753 + 598)

    def test_comparacion_cartera(self):
        # Datos del caso
        total_2023 = 53130
        cartera_2024 = CarteraInversion(2024)
   
        nuevos_proyectos = [
            ProyectoMinero("Reposición Ferrobamba", 1753),
            ProyectoMinero("Coimolache Sulfuros", 598),
            ProyectoMinero("Mina Justa Subterránea", 500),
            ProyectoMinero("Reposición Colquijirca", 431),
            ProyectoMinero("Ampliación Huancapetí", 345),
            ProyectoMinero("Ampliación Huachocolpa", 167)
        ]
        proyectos_anteriores_monto = 53130 - 3794 + 1426
        
        cartera_2024.agregar_proyecto(ProyectoMinero("Total Consolidado", 54556))
        
        diferencia, porcentaje = cartera_2024.comparar_con_año_anterior(total_2023)
        
        self.assertEqual(diferencia, 1426)
        self.assertAlmostEqual(porcentaje, 2.684, places=2) # 2.7% aprox

if __name__ == '__main__':
    unittest.main()
