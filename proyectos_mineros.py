# SISTEMA DE AUDITORIA DE CARTERA MINERA 2024
from typing import List, Tuple
from datetime import datetime

class MineriaError(Exception): pass
class ValidationError(MineriaError): pass

class ProyectoMinero:
    def __init__(self, nombre: str, inversion_millones: float):
        self._validar(nombre, inversion_millones)
        self.nombre = nombre
        self.inversion_millones = inversion_millones
        self.fecha_registro = datetime.now()
        self.historial_cambios = [(inversion_millones, "Registro inicial")]

    def _validar(self, nombre: str, inversion: float):
        if not nombre or len(nombre.strip()) < 3:
            raise ValidationError("Nombre invalido")
        if inversion < 0:
            raise ValidationError("Inversion negativa")

    def actualizar_monto(self, nuevo_monto: float, motivo: str):
        if nuevo_monto < 0:
            raise ValidationError("Monto negativo")
        self.historial_cambios.append((self.inversion_millones, motivo))
        self.inversion_millones = nuevo_monto

class CarteraInversion:
    def __init__(self, año: int):
        self.año = año
        self.proyectos = []

    def agregar_proyecto(self, proyecto: ProyectoMinero):
        self.proyectos.append(proyecto)

    def calcular_total(self) -> float:
        return sum(p.inversion_millones for p in self.proyectos)

    def comparar_con_anterior(self, total_anterior: float) -> Tuple[float, float]:
        if total_anterior < 0: raise ValidationError("Total anterior invalido")
        total_actual = self.calcular_total()
        diferencia = total_actual - total_anterior
        porcentaje = (diferencia / total_anterior) * 100 if total_anterior > 0 else 0
        return diferencia, porcentaje

if __name__ == "__main__":
    cartera = CarteraInversion(2024)
    print("SISTEMA DE GESTION MINERA")
