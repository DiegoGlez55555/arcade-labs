import arcade

"""
This program draws a beach scene with:
- Waves that fade as they approach the shore.
- Birds and clouds moving horizontally.
- A walking stickman with legs, a floating stickman, and a stickman lying on a towel.
- Umbrellas and towels placed on the beach.
"""

# Tamaño de la ventana
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Enhanced Beach Scene"

# Parámetros para las olas
WAVE_STEP = 80  # Distancia entre crestas
WAVE_SPEED = 2  # Velocidad de movimiento horizontal
WAVE_FADE_DISTANCE = 400  # Desaparecen al llegar a la arena

# Parámetros para las nubes y pájaros
CLOUD_SPEED = 1  # Velocidad de las nubes
BIRD_SPEEDS = [2, 3, 1.5, 2.5, 1.8]  # Velocidades individuales de cada pájaro

# Parámetros para los stickmen
STICKMAN_WALK_SPEED = 2  # Velocidad del stickman caminante
STICKMAN_SWIM_SPEED = 1.5  # Velocidad del stickman nadador


class BeachScene(arcade.Window):
    """Clase principal de la escena de la playa."""

    def __init__(self, width, height, title):
        """Inicializa la ventana y los elementos móviles de la escena."""
        super().__init__(width, height, title)

        # Desplazamiento horizontal inicial para las olas
        self.wave_offset = 0

        # Posiciones iniciales de las nubes
        self.cloud_positions = [
            [200, 500],  # Nube 1
            [500, 450],  # Nube 2
            [700, 550]  # Nube 3
        ]

        # Posiciones iniciales de los pájaros
        self.bird_positions = [
            [600, 550],  # Pájaro 1
            [650, 530],  # Pájaro 2
            [700, 560],  # Pájaro 3
            [620, 510],  # Pájaro 4
            [680, 540]  # Pájaro 5
        ]

        # Posición del stickman que camina
        self.walking_stickman_x = 150

        # Posición del stickman que flota (nadando)
        self.swimming_stickman_x = 300

        arcade.set_background_color(arcade.color.AIR_SUPERIORITY_BLUE)

    def on_draw(self):
        """Renderiza todos los elementos gráficos."""
        arcade.start_render()

        # Dibujar los elementos de la escena
        self.draw_scene()

    def on_update(self, delta_time: float):
        """Actualiza las posiciones de los elementos móviles."""
        # Movimiento horizontal de las olas
        self.wave_offset += WAVE_SPEED
        if self.wave_offset > WAVE_STEP:
            self.wave_offset = 0

        # Movimiento horizontal de las nubes
        for cloud in self.cloud_positions:
            cloud[0] += CLOUD_SPEED
            if cloud[0] > SCREEN_WIDTH + 50:
                cloud[0] = -50

        # Movimiento horizontal de los pájaros (con diferentes velocidades)
        for i, bird in enumerate(self.bird_positions):
            bird[0] += BIRD_SPEEDS[i]  # Usando la velocidad específica de cada pájaro
            if bird[0] > SCREEN_WIDTH + 50:
                bird[0] = -50

        # Movimiento del stickman caminante
        self.walking_stickman_x += STICKMAN_WALK_SPEED
        if self.walking_stickman_x > SCREEN_WIDTH + 50:
            self.walking_stickman_x = -50

        # Movimiento del stickman nadador (flotando)
        self.swimming_stickman_x += STICKMAN_SWIM_SPEED
        if self.swimming_stickman_x > SCREEN_WIDTH + 50:
            self.swimming_stickman_x = -50

    def draw_scene(self):
        """Dibuja todos los elementos estáticos y dinámicos."""
        # Fondo: arena, agua, sol
        self.draw_background()

        # Dibujar las olas dinámicas
        self.draw_waves()

        # Sombrillas y toallas
        self.draw_umbrellas_and_towels()

        # Dibujar las nubes
        self.draw_clouds()

        # Dibujar los pájaros
        self.draw_birds()

        # Dibujar los stickmen
        self.draw_stickmen()

    def draw_background(self):
        """Dibuja el fondo de la escena."""
        # Dibujar la arena
        arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, 200, 0, arcade.color.SAND)

        # Dibujar el agua
        arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, 300, 200, arcade.color.BLUE_SAPPHIRE)

        # Dibujar el sol
        arcade.draw_circle_filled(100, 500, 50, arcade.color.YELLOW)

    def draw_waves(self):
        """Dibuja múltiples líneas de olas que se desvanecen al acercarse a la arena."""
        for i in range(-1, int(SCREEN_WIDTH / WAVE_STEP) + 2):  # Ajusta las olas en horizontal
            x_start = i * WAVE_STEP - self.wave_offset
            x_mid = x_start + WAVE_STEP / 2
            x_end = x_start + WAVE_STEP
            y_base = 250  # Altura base de las olas

            # Cada ola se dibuja y desvanecerá progresivamente al acercarse al terreno de la arena (Y=200)
            fade_factor = max(0, WAVE_FADE_DISTANCE - (y_base - 200))  # Basado en distancia vertical
            alpha = int(255 * (fade_factor / WAVE_FADE_DISTANCE))  # Ajusta la opacidad

            # Asegurar que la opacidad esté entre 0 y 255
            alpha = max(0, min(alpha, 255))

            # Color de la ola con transparencia aplicada
            wave_color = (64, 224, 208, alpha)

            # Dibujar cada segmento de la onda
            arcade.draw_line(x_start, y_base, x_mid, y_base + 20, wave_color, 2)
            arcade.draw_line(x_mid, y_base + 20, x_end, y_base, wave_color, 2)

    def draw_umbrellas_and_towels(self):
        """Dibuja sombrillas y toallas."""
        # Sombrilla 1
        arcade.draw_line(300, 200, 300, 250, arcade.color.BROWN, 4)
        arcade.draw_arc_filled(300, 250, 80, 40, arcade.color.RED, 0, 180)
        arcade.draw_circle_filled(300, 270, 5, arcade.color.RED)

        # Sombrilla 2
        arcade.draw_line(500, 200, 500, 250, arcade.color.BROWN, 4)
        arcade.draw_arc_filled(500, 250, 80, 40, arcade.color.BLUE, 0, 180)
        arcade.draw_circle_filled(500, 270, 5, arcade.color.BLUE)

        # Dibujar toallas
        arcade.draw_lrtb_rectangle_filled(350, 400, 190, 160, arcade.color.YELLOW)
        arcade.draw_lrtb_rectangle_filled(600, 650, 190, 160, arcade.color.PURPLE)

    def draw_clouds(self):
        """Dibuja nubes."""
        for x, y in self.cloud_positions:
            arcade.draw_circle_filled(x - 30, y - 10, 30, arcade.color.WHITE)
            arcade.draw_circle_filled(x, y, 40, arcade.color.WHITE)
            arcade.draw_circle_filled(x + 30, y - 10, 30, arcade.color.WHITE)

    def draw_birds(self):
        """Dibuja pájaros."""
        for x, y in self.bird_positions:
            arcade.draw_arc_outline(x, y, 40, 20, arcade.color.WHITE, 0, 90, 3)
            arcade.draw_arc_outline(x + 40, y, 40, 20, arcade.color.WHITE, 90, 180, 3)

    def draw_stickmen(self):
        """Dibuja los stickmen."""
        # Stickman caminando (con piernas), más abajo para no pisar al stickman tumbado
        arcade.draw_circle_filled(self.walking_stickman_x, 140, 10, arcade.color.BLACK)
        arcade.draw_line(self.walking_stickman_x, 130, self.walking_stickman_x, 100, arcade.color.BLACK, 2)
        arcade.draw_line(self.walking_stickman_x, 120, self.walking_stickman_x - 10, 110, arcade.color.BLACK, 2)
        arcade.draw_line(self.walking_stickman_x, 120, self.walking_stickman_x + 10, 110, arcade.color.BLACK, 2)
        arcade.draw_line(self.walking_stickman_x - 5, 100, self.walking_stickman_x - 10, 80, arcade.color.BLACK, 2)
        arcade.draw_line(self.walking_stickman_x + 5, 100, self.walking_stickman_x + 10, 90, arcade.color.BLACK, 2)

        # Stickman nadando (flotando)
        arcade.draw_circle_filled(self.swimming_stickman_x, 260, 10, arcade.color.BLACK)  # Cabeza
        arcade.draw_line(self.swimming_stickman_x, 250, self.swimming_stickman_x, 230, arcade.color.BLACK, 2)  # Cuerpo
        arcade.draw_line(self.swimming_stickman_x, 245, self.swimming_stickman_x - 10, 250, arcade.color.BLACK,
                         2)  # Brazo izq
        arcade.draw_line(self.swimming_stickman_x, 245, self.swimming_stickman_x + 10, 250, arcade.color.BLACK,
                         2)  # Brazo der

        # Stickman tumbado
        arcade.draw_circle_filled(375, 175, 10, arcade.color.BLACK)
        arcade.draw_line(365, 175, 335, 175, arcade.color.BLACK, 2)
        arcade.draw_line(335, 175, 320, 185, arcade.color.BLACK, 2)
        arcade.draw_line(335, 175, 320, 165, arcade.color.BLACK, 2)
        arcade.draw_line(365, 175, 380, 185, arcade.color.BLACK, 2)
        arcade.draw_line(365, 175, 380, 165, arcade.color.BLACK, 2)


def main():
    """Ejecuta la escena."""
    window = BeachScene(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()


if __name__ == "__main__":
    main()
