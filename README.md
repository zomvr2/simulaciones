# Simulaciones de Prueba - Universidad

Este repositorio contiene simulaciones y ejercicios prácticos desarrollados como parte de las pruebas académicas de programación en la universidad.

## Estructura del Proyecto

```
simulaciones/
├── simulacion1/
│   ├── datos.txt        # Datos de entrada para ejercicio 1
│   ├── invocador.txt    # Datos de entrada para ejercicio 3
│   ├── ejercicio1.py    # Análisis de datos de contagios por continente
│   ├── ejercicio2.py    # Sistema de votación interactivo
│   └── ejercicio3.py    # Análisis de estadísticas de videojuegos
└── README.md
```

## Descripción de las Simulaciones

### Simulación 1

Esta simulación incluye tres ejercicios diferentes que demuestran conceptos fundamentales de programación:

#### Ejercicio 1: Análisis de Datos de Contagios
- **Archivo**: `ejercicio1.py`
- **Datos de entrada**: `datos.txt`
- **Descripción**: Procesa datos de contagios por país y continente, calculando estadísticas como:
  - Total de contagios
  - País con mayor/menor número de casos por continente
  - País con más recuperados
  - País con menos muertes

#### Ejercicio 2: Sistema de Votación
- **Archivo**: `ejercicio2.py`
- **Descripción**: Implementa un sistema interactivo de votación donde:
  - Se registran votos para eliminar participantes (Viviana, Constanza, Jennifer)
  - Valida formato de entrada con código "3331"
  - Determina quién debe ser eliminado según los votos

#### Ejercicio 3: Estadísticas de Videojuegos
- **Archivo**: `ejercicio3.py`
- **Datos de entrada**: `invocador.txt`
- **Descripción**: Analiza estadísticas de un jugador incluyendo:
  - Tipos de partidas jugadas (Normal, Solo, Flex)
  - Carriles preferidos (Top, Mid, Jungle, ADC, Support)
  - KDA (Kill/Death/Assist ratio)
  - Porcentaje de victorias en partidas clasificatorias

## Requisitos

- Python 3.x
- Archivos de datos (`datos.txt`, `invocador.txt`) en la carpeta correspondiente

## Cómo Ejecutar

1. Navega a la carpeta `simulacion1`:
   ```bash
   cd simulacion1
   ```

2. Ejecuta el ejercicio deseado:
   ```bash
   python ejercicio1.py
   python ejercicio2.py
   python ejercicio3.py
   ```

## Formato de Datos

### datos.txt
Formato de entrada para el ejercicio 1:
```
Continente,NumPaises
Pais,Poblacion,Contagios,Recuperados,Muertes
...
```

### invocador.txt
Contiene datos de partidas y estadísticas del jugador para el ejercicio 3.