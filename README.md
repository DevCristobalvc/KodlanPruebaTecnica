# KodlanPruebaTecnica

# Invasión Espacial

Invasión Espacial es un juego arcade simple pero entretenido, creado con PyGame. El jugador controla una nave espacial en la parte inferior de la pantalla y debe esquivar y destruir a una oleada de enemigos que se aproximan desde la parte superior. Con cada enemigo destruido, el jugador acumula puntos, buscando alcanzar el mayor puntaje posible antes de que los enemigos lleguen a la base de la pantalla o colisionen con la nave.

## Características

- Control simple utilizando las teclas de flecha para moverse y la barra espaciadora para disparar.
- Enemigos con movimientos aleatorios que aumentan la dificultad del juego gradualmente.
- Sistema de puntuación para aumentar la competitividad.

## Cómo Jugar

- **Mover la nave:** Usa las teclas de flecha izquierda y derecha para mover tu nave a lo largo de la parte inferior de la pantalla.
- **Disparar:** Presiona la barra espaciadora para disparar a los enemigos.
- **Evitar enemigos y proyectiles:** Esquiva los enemigos y sus disparos para sobrevivir el mayor tiempo posible.

## Instalación

Para ejecutar este juego, necesitarás Python y PyGame instalado en tu computadora. Sigue estos pasos para configurarlo:

1. Asegúrate de tener Python instalado en tu sistema. Si no lo tienes, puedes descargarlo desde [python.org](https://www.python.org/downloads/).

2. Instala PyGame. Abre tu terminal o línea de comandos y ejecuta el siguiente comando:
    ```
    pip install pygame
    ```

3. Clona este repositorio o descarga el código fuente a tu máquina local.

4. Navega hasta la carpeta del proyecto en tu terminal o línea de comandos y ejecuta el archivo `main.py` con Python:
    ```
    python src/main.py
    ```

## Estructura del Proyecto

El proyecto está organizado en múltiples archivos para facilitar su mantenimiento y escalabilidad:

- `main.py`: Punto de entrada del juego que inicia la clase Game.
- `game.py`: Contiene la lógica principal del juego, incluyendo el bucle del juego.
- `player.py`: Define la clase Player con la lógica para controlar la nave del jugador.
- `enemy.py`: Define la clase Enemy para controlar los enemigos.
- `settings.py`: Almacena configuraciones básicas del juego, como dimensiones de la pantalla y colores.
- `assets/`: Contiene subcarpetas para imágenes (`images/`) y sonidos (`sounds/`), incluyendo sprites de la nave, enemigos, y efectos de sonido.

¡Esperamos que disfrutes jugando y modificando Invasión Espacial!
