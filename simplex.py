from scipy.optimize import linprog

def optimizar_tratamientos(tratamientos, pesos):
    # Fórmula de utilidad ponderada
    c = [
        -(t["efectividad"] * pesos["efectividad"] +
          t["costo"] * pesos["costo"] +
          t["tiempo"] * pesos["tiempo"])
        for t in tratamientos
    ]
    result = linprog(c, bounds=[(0, 1)] * len(tratamientos), method="highs")
    if result.success:
        print("Tratamientos seleccionados:")
        for i, valor in enumerate(result.x):
            if valor > 0.5:
                t = tratamientos[i]
                print(f"- {t['nombre']} (Efectividad: {t['efectividad']}, Costo: {t['costo']}, Tiempo: {t['tiempo']})")
    else:
        print("No se pudo optimizar los tratamientos.")
