import time
from proyectos_mineros import ProyectoMinero, CarteraInversion

def ejecutar_stress_test(cantidad_proyectos=100000):
    print(f"--- INICIANDO PRUEBA DE ESTRÉS: {cantidad_proyectos} Registros ---")
    cartera = CarteraInversion(2024)

    start_time = time.time()
    try:
        for i in range(cantidad_proyectos):
            p = ProyectoMinero(f"Proyecto Stress {i}", float(i * 1.5))
            cartera.agregar_proyecto(p)
        
        end_time = time.time()
        print(f"✅ Inserción completada en: {end_time - start_time:.4f} segundos")
        
    except MemoryError:
        print("❌ FALLO: El sistema agotó la memoria RAM.")
        return

    start_time = time.time()
    total = cartera.calcular_total()
    end_time = time.time()
    print(f"✅ Cálculo de total completado en: {end_time - start_time:.4f} segundos")
    print(f"Resultado final: US$ {total:,.2f} M")


    print("\nEstrés de Auditoría (10,000 actualizaciones en un proyecto) ")
    if cartera.proyectos:
        proyecto_critico = cartera.proyectos[0]
        start_time = time.time()
        for i in range(10000):
            proyecto_critico.actualizar_monto(float(i), "Actualización masiva de estrés")
        end_time = time.time()
        print(f"✅ Auditoría completada en: {end_time - start_time:.4f} segundos")
        print(f"Tamaño del historial: {len(proyecto_critico.historial_cambios)} registros")

if __name__ == "__main__":
    ejecutar_stress_test()
