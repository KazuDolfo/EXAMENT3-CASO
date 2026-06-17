# Requerimiento: Gestión de Cartera de Inversión Minera
# Historia de Usuario:
# Como Analista del MINEM, quiero un sistema que me permita registrar proyectos mineros 
# con sus montos de inversión para calcular el total de la cartera y compararlo con el 
# año anterior, de modo que pueda reportar el crecimiento del sector.

class ProyectoMinero:
    def __init__(self, nombre, inversion_millones):
        self.nombre = nombre
        self.inversion_millones = inversion_millones

class CarteraInversion:
    def __init__(self, año, proyectos=None):
        self.año = año
        self.proyectos = proyectos if proyectos else []

    def agregar_proyecto(self, proyecto):
        self.proyectos.append(proyecto)

    def calcular_total_inversion(self):
        return sum(p.inversion_millones for p in self.proyectos)

    def comparar_con_año_anterior(self, total_anterior):
        total_actual = self.calcular_total_inversion()
        diferencia = total_actual - total_anterior
        porcentaje = (diferencia / total_anterior) * 100 if total_anterior != 0 else 0
        return diferencia, porcentaje
