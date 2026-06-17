from typing import List, Tuple, Optional
from datetime import datetime

class MineriaError(Exception):
    """Clase base para excepciones del sistema."""
    pass

class ValidationError(MineriaError):
    """Excepción para errores de validación de datos."""
    pass

class ProyectoMinero:
    def __init__(self, nombre: str, inversion_millones: float):
        self._validar(nombre, inversion_millones)
        self.nombre = nombre
        self.inversion_millones = inversion_millones
        self.fecha_registro = datetime.now()
        self.historial_cambios: List[Tuple[float, str]] = [(inversion_millones, "Registro inicial")]

    def _validar(self, nombre: str, inversion: float):
        if not nombre or len(nombre.strip()) < 3:
            raise ValidationError("El nombre del proyecto debe tener al menos 3 caracteres.")
        if inversion < 0:
            raise ValidationError("La inversión no puede ser negativa.")

    def actualizar_monto(self, nuevo_monto: float, motivo: str):
        if nuevo_monto < 0:
            raise ValidationError("El nuevo monto no puede ser negativo.")
        self.historial_cambios.append((self.inversion_millones, motivo))
        self.inversion_millones = nuevo_monto

class CarteraInversion:
    def __init__(self, año: int):
        self.año = año
        self.proyectos: List[ProyectoMinero] = []

    def agregar_proyecto(self, proyecto: ProyectoMinero):
        self.proyectos.append(proyecto)

    def calcular_total(self) -> float:
        return sum(p.inversion_millones for p in self.proyectos)

    def comparar_con_anterior(self, total_anterior: float) -> Tuple[float, float]:
        if total_anterior < 0:
            raise ValidationError("El total anterior no puede ser negativo.")
        total_actual = self.calcular_total()
        diferencia = total_actual - total_anterior
        porcentaje = (diferencia / total_anterior) * 100 if total_anterior > 0 else 0
        return diferencia, porcentaje

def ejecutar_cli():
    cartera = CarteraInversion(2024)
    print("--- SISTEMA MINERO PRO (QA READY) ---")
    # Datos semilla
    try:
        cartera.agregar_proyecto(ProyectoMinero("Reposición Ferrobamba", 1753))
        cartera.agregar_proyecto(ProyectoMinero("Mina Justa Subterránea", 500))
    except ValidationError as e:
        print(f"Error de inicialización: {e}")

    while True:
        print("\n1. Ver Cartera | 2. Registrar Proyecto | 3. Actualizar Monto | 4. Salir")
        opt = input("Seleccione: ")
        
        if opt == "1":
            print(f"\nCartera {cartera.año}: US$ {cartera.calcular_total():,.2f} M")
            for p in cartera.proyectos:
                print(f"- {p.nombre}: US$ {p.inversion_millones} M")
        elif opt == "2":
            try:
                nom = input("Nombre: ")
                monto = float(input("Inversión (M USD): "))
                cartera.agregar_proyecto(ProyectoMinero(nom, monto))
                print("Éxito: Proyecto registrado.")
            except (ValidationError, ValueError) as e:
                print(f"Error de Validación: {e}")
        elif opt == "3":
            nom = input("Nombre del proyecto a editar: ")
            p = next((p for p in cartera.proyectos if p.nombre.lower() == nom.lower()), None)
            if p:
                try:
                    nuevo = float(input("Nuevo monto: "))
                    motivo = input("Motivo del cambio: ")
                    p.actualizar_monto(nuevo, motivo)
                    print("Éxito: Monto actualizado y auditado.")
                except ValidationError as e:
                    print(f"Error: {e}")
            else:
                print("Proyecto no encontrado.")
        elif opt == "4":
            break

if __name__ == "__main__":
    ejecutar_cli()
