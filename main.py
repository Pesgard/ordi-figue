from perceptron import entrenar_perceptron, diagnosticar
from arbol import entrenar_arbol, determinar_pesos
from saw import saw

# Enfermedades y tratamientos
enfermedades = ["Gripe", "Resfriado", "Migraña", "Fatiga"]
tratamientos = {
    "Gripe": [
        {"nombre": "Antivirales", "effectiveness": 8, "cost": 6, "time": 5, "inyeccion": 1},
        {"nombre": "Reposo y líquidos", "effectiveness": 6, "cost": 10, "time": 9, "inyeccion": 0},
    ],
    "Resfriado": [
        {"nombre": "Analgésicos", "effectiveness": 7, "cost": 4, "time": 7, "inyeccion": 0},
        {"nombre": "Reposo", "effectiveness": 5, "cost": 9, "time": 10, "inyeccion": 0},
    ],
    "Migraña": [
        {"nombre": "Triptanes", "effectiveness": 9, "cost": 7, "time": 4, "inyeccion": 0},
        {"nombre": "Analgésicos fuertes", "effectiveness": 8, "cost": 6, "time": 6, "inyeccion": 0},
    ],
    "Fatiga": [
        {"nombre": "Vitaminas y minerales", "effectiveness": 6, "cost": 5, "time": 8, "inyeccion": 1},
        {"nombre": "Reposo programado", "effectiveness": 5, "cost": 3, "time": 10, "inyeccion": 0},
    ],
}

def main():
    # Entrenar modelos
    modelo_perceptron = entrenar_perceptron()
    modelo_arbol = entrenar_arbol()

    # Preguntar síntomas
    sintomas = []
    preguntas = [
        "¿Tienes fiebre? (1 para Sí, 0 para No): ",
        "¿Tienes tos? (1 para Sí, 0 para No): ",
        "¿Tienes dolor de cabeza? (1 para Sí, 0 para No): ",
        "¿Tienes dolor muscular? (1 para Sí, 0 para No): ",
        "¿Tienes congestión nasal? (1 para Sí, 0 para No): ",
        "¿Te sientes cansado? (1 para Sí, 0 para No): "
    ]
    for pregunta in preguntas:
        sintomas.append(int(input(pregunta)))

    # Diagnóstico especial para "Fatiga" y "Saludable"
    if sum(sintomas) == 1 and sintomas[-1] == 1:  # Solo está cansado
        enfermedad = "Fatiga"
    elif sum(sintomas) == 0:  # Ningún síntoma
        print("Diagnóstico: Saludable")
        print("No hay necesidad de tratamientos.")
        return
    else:
        # Diagnóstico normal
        enfermedad = diagnosticar(modelo_perceptron, sintomas, enfermedades)

    print(f"El modelo perceptron Diagnosticó: {enfermedad}")

    # Consultar preferencias solo si no está saludable
    preferencias = [
        int(input("¿Prefieres tratamientos más efectivos? (1 para Sí, 0 para No): ")),
        int(input("¿Prefieres tratamientos con inyecciones? (1 para Sí, 0 para No): ")),
        int(input("¿Prefieres tratamientos más cómodos (fáciles de seguir)? (1 para Sí, 0 para No): ")),
    ]
    pesos = determinar_pesos(modelo_arbol, preferencias)
    print(f"El arbol de decision asigno los Pesos correspondientes: {pesos}")

    # Optimización de tratamientos
    if enfermedad in tratamientos:
        print("Se aplico el metodo saw para la Optimización de tratamientos:")
        tratamientos_optimizados = saw(tratamientos[enfermedad], pesos)
        print("Tratamientos seleccionados:")
        for t in tratamientos_optimizados:
            print(f"- {t['nombre']} (Efectividad: {t['effectiveness']}, Costo: {t['cost']}, Tiempo: {t['time']})")
    else:
        print("No se encontraron tratamientos para la enfermedad.")

if __name__ == "__main__":
    main()
