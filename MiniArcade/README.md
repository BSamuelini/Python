# MiniArcade 🎮

MiniArcade es un pequeño recopilatorio de minijuegos en consola escritos en Python.  
Permite jugar a tres juegos clásicos desde un menú y guarda un registro de las partidas en un fichero de texto.

## Juegos incluidos

### 1. Piedra, Papel o Tijera (PPT)

- Juegas contra un bot.
- Controles:
  - `p` → Piedra  
  - `a` → Papel  
  - `t` → Tijera  
  - `s` → Salir de la partida
- El juego muestra al final:
  - Rondas jugadas  
  - Victorias  
  - Puntuación (más alta si ganas muchas rondas rápido)

### 2. Adivina el número

- Dificultades disponibles:
  - `1` → **normal** (1–20)  
  - `2` → **noob** (1–50)  
  - `3` → **pro** (1–100)  
  - `4` → **hacker** (1–1.000.000)  
- El programa elige un número al azar y tú intentas adivinarlo.
- `0` → rendirse.
- Mensajes durante la partida:
  - “Bajo” → tu número es menor que el secreto.
  - “Alto” → tu número es mayor que el secreto.
- Al acertar muestra:
  - Número de intentos  
  - Puntuación calculada según intentos y tiempo

### 3. Ahorcado

- Niveles:
  - `1` → ES Fácil  
  - `2` → ES Difícil  
  - `3` → VA Fácil (valenciano)  
  - `4` → VA Difícil (valenciano)  
- Palabras de ejemplo:
  - ES: `gato`, `sol`, `casa`, `programa`, `ordenador`
  - VA: `gos`, `sol`, `casa`, `ordinador`, `programacio`
- Mecánica:
  - Cuentas con **6 intentos**.
  - Se muestran las letras acertadas y las incorrectas usadas.
  - Introduces una letra en cada turno.
- Final de partida:
  - Si ganas → muestra la palabra y una puntuación.
  - Si pierdes → muestra la palabra correcta.

---

## Requisitos

- **Python 3** (recomendado 3.8 o superior)
- Una terminal
- No se usan librerías externas, solo módulos estándar (`os`, `time`, `random`).

---

## Cómo ejecutar

1. Sitúate en la carpeta donde está `MiniArcade.py`.
2. Ejecuta:

```bash
python3 MiniArcade.py
