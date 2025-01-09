def saw(treatments, weights):
    """
    Calcula el puntaje SAW para cada tratamiento y los ordena por puntaje.
    :param treatments: Lista de tratamientos con sus atributos.
    :param weights: Diccionario con los pesos asignados ('efectividad', 'inyeccion', 'comodidad').
    :return: Lista de tratamientos ordenados por puntaje SAW.
    """
    # Normalizar atributos
    normalized_matrix = []
    for t in treatments:
        normalized_matrix.append([
            t["effectiveness"] / max(tr["effectiveness"] for tr in treatments),
            t["inyeccion"],  # Este valor es binario, no necesita normalización
            t["time"] / max(tr["time"] for tr in treatments),
        ])

    # Calcular puntaje ponderado
    scores = []
    for i, t in enumerate(treatments):
        score = (
            normalized_matrix[i][0] * weights["efectividad"] +
            normalized_matrix[i][1] * weights["inyeccion"] +
            normalized_matrix[i][2] * weights["comodidad"]
        )
        scores.append((score, t))

    # Ordenar tratamientos por puntaje SAW
    scores.sort(reverse=True, key=lambda x: x[0])
    return [treatment for _, treatment in scores]
