import arcade

# --- Constantes ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
MOVEMENT_SPEED = 5  # Velocidad de movimiento del stickman principal


class MyGame(arcade.Window):
    """ Clase principal del juego """

    def __init__(self):
        """ Inicializador """
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Mover al Stickman con Fondo y Objetos")

        # Configurar el color de fondo
        arcade.set_background_color(arcade.color.AIR_SUPERIORITY_BLUE)

        # Posición inicial del stickman principal
        self.stickman_x = 400
        self.stickman_y = 300

    def on_draw(self):
        """ Método para renderizar/dibujar todo en pantalla """
        # Empezar a renderizar
        arcade.start_render()

        # Dibujar el fondo (todos los objetos estáticos)
        self.draw_background()

        # Dibujar el stickman principal
        self.draw_stickman(self.stickman_x, self.stickman_y)

    def on_key_press(self, key, modifiers):
        """ Manejo de teclas presionadas para mover al stickman """
        if key == arcade.key.UP:
            self.stickman_y += MOVEMENT_SPEED
        elif key == arcade.key.DOWN:
            self.stickman_y -= MOVEMENT_SPEED
        elif key == arcade.key.LEFT:
            self.stickman_x -= MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.stickman_x += MOVEMENT_SPEED

    def draw_background(self):
        """ Dibuja el fondo estático (playa, olas, sol, sombrillas, etc.) """
        # Dibujar la playa
        arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, 200, 0, arcade.color.SAND)
        arcade.draw_lrtb_rectangle_filled(0, SCREEN_WIDTH, 300, 200, arcade.color.BLUE_SAPPHIRE)

        # Dibujar el sol
        arcade.draw_circle_filled(100, 500, 50, arcade.color.YELLOW)

        # Dibujar olas
        wave_color = (102, 153, 200)
        wave_points = [
            (0, 300),
            (100, 310),
            (200, 290),
            (300, 310),
            (400, 290),
            (500, 310),
            (600, 290),
            (700, 310),
            (800, 300)
        ]
        arcade.draw_polygon_filled([(0, 300)] + wave_points + [(800, 200), (0, 200)], arcade.color.BLUE_SAPPHIRE)

        # Dibujar bordes de las olas
        arcade.draw_line_strip(wave_points, color=arcade.color.BLUE_SAPPHIRE, line_width=3)
        arcade.draw_line_strip(
            [(0, 230), (100, 240), (200, 220), (300, 240), (400, 220), (500, 240), (600, 220), (700, 240), (800, 230)],
            color=wave_color,
            line_width=3
        )
        arcade.draw_line_strip(
            [(0, 260), (100, 270), (200, 250), (300, 270), (400, 250), (500, 270), (600, 250), (700, 270), (800, 260)],
            color=wave_color,
            line_width=3
        )

        # Dibujar nubes
        clouds = [
            [(200, 500), (230, 510, 40), (260, 500)],
            [(500, 450), (530, 460, 40), (560, 450)],
            [(700, 550), (730, 560, 40), (760, 550)],
        ]
        for cloud in clouds:
            arcade.draw_circle_filled(cloud[0][0], cloud[0][1], 30, arcade.color.WHITE)
            arcade.draw_circle_filled(cloud[1][0], cloud[1][1], 40, arcade.color.WHITE)
            arcade.draw_circle_filled(cloud[2][0], cloud[2][1], 30, arcade.color.WHITE)

        # Dibujar pájaros
        bird_positions = [(600, 550), (650, 530), (700, 560), (620, 510), (680, 540)]
        for x, y in bird_positions:
            arcade.draw_arc_outline(x, y, 40, 20, arcade.color.BLACK, 0, 90, 2)
            arcade.draw_arc_outline(x + 40, y, 40, 20, arcade.color.BLACK, 90, 180, 2)

        # Dibujar sombrillas
        arcade.draw_line(300, 200, 300, 250, arcade.color.BROWN, 4)
        arcade.draw_arc_filled(300, 250, 80, 40, arcade.color.RED, 0, 180)
        arcade.draw_circle_filled(300, 270, 5, arcade.color.RED)
        arcade.draw_line(500, 200, 500, 250, arcade.color.BROWN, 4)
        arcade.draw_arc_filled(500, 250, 80, 40, arcade.color.BLUE, 0, 180)
        arcade.draw_circle_filled(500, 270, 5, arcade.color.BLUE)

        # Dibujar toallas
        arcade.draw_lrtb_rectangle_filled(350, 400, 190, 160, arcade.color.YELLOW_ORANGE)  # Toalla amarilla
        arcade.draw_lrtb_rectangle_filled(600, 650, 190, 160, arcade.color.BABY_BLUE)  # Toalla azul

        # Dibujar stickmans adicionales
        self.draw_stickman(150, 220)  # Stickman 1
        self.draw_stickman(375, 175)  # Stickman 2

    def draw_stickman(self, x, y):
        """ Dibuja un stickman en la posición (x, y) """
        # Cabeza
        arcade.draw_circle_filled(x, y + 30, 10, arcade.color.BLACK)

        # Cuerpo
        arcade.draw_line(x, y + 20, x, y - 20, arcade.color.BLACK, 2)

        # Brazos
        arcade.draw_line(x, y + 10, x - 10, y - 10, arcade.color.BLACK, 2)  # Brazo izquierdo
        arcade.draw_line(x, y + 10, x + 10, y - 10, arcade.color.BLACK, 2)  # Brazo derecho

        # Piernas
        arcade.draw_line(x, y - 20, x - 10, y - 30, arcade.color.BLACK, 2)  # Pierna izquierda
        arcade.draw_line(x, y - 20, x + 10, y - 30, arcade.color.BLACK, 2)  # Pierna derecha


def main():
    """ Método principal """
    window = MyGame()
    arcade.run()


main()
