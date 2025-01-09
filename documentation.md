# API Documentation

## Diagnosticar Enfermedad

**Endpoint:** `/diagnosticar`  
**Method:** `POST`  
**Description:** Receives a list of symptoms and returns the diagnosis.

### Request:
```json
{
  "sintomas": [1, 0, 1, 0, 1, 0]
}
```

### Response:
```json
{
  "diagnostico": "Gripe"
}
```

## Determinar Pesos

**Endpoint:** `/determinar_pesos`  
**Method:** `POST`  
**Description:** Receives a list of preferences and returns the weights for treatment optimization.

### Request:
```json
{
  "preferencias": [1, 0, 1]
}
```

### Response:
```json
{
  "pesos": {
    "efectividad": 0.6,
    "inyeccion": 0.3,
    "comodidad": 0.1
  }
}
```

## Optimizar Tratamientos

**Endpoint:** `/optimizar_tratamientos`  
**Method:** `POST`  
**Description:** Receives a disease and weights, and returns the optimized treatments.

### Request:
```json
{
  "enfermedad": "Gripe",
  "pesos": {
    "efectividad": 0.6,
    "inyeccion": 0.3,
    "comodidad": 0.1
  }
}
```

### Response:
```json
{
  "tratamientos": [
    {
      "nombre": "Antivirales",
      "effectiveness": 8,
      "cost": 6,
      "time": 5,
      "inyeccion": 1
    },
    {
      "nombre": "Reposo y líquidos",
      "effectiveness": 6,
      "cost": 10,
      "time": 9,
      "inyeccion": 0
    }
  ]
}
```