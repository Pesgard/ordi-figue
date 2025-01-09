from sklearn.tree import DecisionTreeClassifier

def entrenar_arbol():
    # Datos de entrenamiento ampliados
    # X representa las combinaciones de preferencias
    # Cada fila es una combinación de: [efectividad, inyección, comodidad]
    X = [
        [1, 0, 0],  # Prefiere efectividad, no inyecciones, no comodidad
        [0, 1, 0],  # Prefiere inyecciones
        [0, 0, 1],  # Prefiere comodidad
        [1, 1, 0],  # Prefiere efectividad e inyecciones
        [1, 0, 1],  # Prefiere efectividad y comodidad
        [0, 1, 1],  # Prefiere inyecciones y comodidad
    ]
    # y representa las combinaciones de pesos que el árbol devolverá
    y = [0, 1, 2, 0, 0, 2]  # Índices para los pesos

    modelo = DecisionTreeClassifier()
    modelo.fit(X, y)
    return modelo

def determinar_pesos(modelo, preferencias):
    # Predecir índice de pesos basado en las preferencias
    prediccion = modelo.predict([preferencias])[0]
    # Lista actualizada de pesos
    pesos_opciones = [
        {"efectividad": 0.6, "inyeccion": 0.3, "comodidad": 0.1},  # Más efectividad
        {"efectividad": 0.3, "inyeccion": 0.6, "comodidad": 0.1},  # Más inyecciones
        {"efectividad": 0.3, "inyeccion": 0.2, "comodidad": 0.5},  # Más comodidad
    ]
    return pesos_opciones[prediccion]
