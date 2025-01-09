from sklearn.linear_model import Perceptron


def entrenar_perceptron():
    # Datos de entrenamiento actualizados para 6 características
    X = [
        [1, 1, 1, 0, 1, 0],  # Ejemplo para enfermedad 0
        [0, 1, 0, 1, 0, 1],  # Ejemplo para enfermedad 1
        [0, 0, 1, 1, 1, 0],  # Ejemplo para enfermedad 2
        [0, 0, 0, 0, 0, 1]  # Ejemplo para enfermedad 3
    ]
    y = [0, 1, 2, 3]  # Índices de enfermedades
    model = Perceptron()
    model.fit(X, y)
    return model


def diagnosticar(modelo, sintomas, enfermedades):
    # Validar que los síntomas tengan el tamaño esperado
    if len(sintomas) != 6:
        raise ValueError("El número de síntomas debe ser exactamente 6.")

    # Realizar predicción
    prediccion = modelo.predict([sintomas])[0]
    return enfermedades[prediccion]
