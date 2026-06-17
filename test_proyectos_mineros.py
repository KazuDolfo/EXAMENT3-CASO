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
        
        # Simulamos que llegamos al total de 54556
        # No agregamos todos los 51 proyectos por brevedad, pero seteamos el total esperado
        # O mejor, agregamos los nuevos proyectos mencionados
        nuevos_proyectos = [
            ProyectoMinero("Reposición Ferrobamba", 1753),
            ProyectoMinero("Coimolache Sulfuros", 598),
            ProyectoMinero("Mina Justa Subterránea", 500),
            ProyectoMinero("Reposición Colquijirca", 431),
            ProyectoMinero("Ampliación Huancapetí", 345),
            ProyectoMinero("Ampliación Huachocolpa", 167)
        ]
        proyectos_anteriores_monto = 53130 - 3794 + 1426 # Esto es solo para cuadrar con los datos del texto
        # El texto dice: 2024 (54556) - 2023 (53130) = 1426 (2.7%)
        
        cartera_2024.agregar_proyecto(ProyectoMinero("Total Consolidado", 54556))
        
        diferencia, porcentaje = cartera_2024.comparar_con_año_anterior(total_2023)
        
        self.assertEqual(diferencia, 1426)
        self.assertAlmostEqual(porcentaje, 2.684, places=2) # 2.7% aprox

if __name__ == '__main__':
    unittest.main()
