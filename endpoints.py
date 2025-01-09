from flask import Flask, request, jsonify
from flask_cors import CORS
from perceptron import entrenar_perceptron, diagnosticar
from arbol import entrenar_arbol, determinar_pesos
from saw import saw

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

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

# Entrenar modelos
modelo_perceptron = entrenar_perceptron()
modelo_arbol = entrenar_arbol()

@app.route('/diagnosticar', methods=['POST'])
def diagnosticar_enfermedad():
    sintomas = request.json.get('sintomas')
    if len(sintomas) != 6:
        return jsonify({"error": "El número de síntomas debe ser exactamente 6."}), 400

    if sum(sintomas) == 1 and sintomas[-1] == 1:
        enfermedad = "Fatiga"
    elif sum(sintomas) == 0:
        return jsonify({"diagnostico": "Saludable", "tratamientos": []})
    else:
        enfermedad = diagnosticar(modelo_perceptron, sintomas, enfermedades)

    return jsonify({"diagnostico": enfermedad})

@app.route('/determinar_pesos', methods=['POST'])
def obtener_pesos():
    preferencias = request.json.get('preferencias')
    if len(preferencias) != 3:
        return jsonify({"error": "El número de preferencias debe ser exactamente 3."}), 400

    pesos = determinar_pesos(modelo_arbol, preferencias)
    return jsonify({"pesos": pesos})

@app.route('/optimizar_tratamientos', methods=['POST'])
def optimizar_tratamientos():
    data = request.json
    enfermedad = data.get('enfermedad')
    pesos = data.get('pesos')

    if enfermedad not in tratamientos:
        return jsonify({"error": "No se encontraron tratamientos para la enfermedad."}), 400

    tratamientos_optimizados = saw(tratamientos[enfermedad], pesos)
    return jsonify({"tratamientos": tratamientos_optimizados})

if __name__ == "__main__":
    app.run(debug=True)