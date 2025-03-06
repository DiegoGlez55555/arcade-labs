import arcade
import random

# --- Constantes ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BALL_SPEED_MIN = 2  # Velocidad mínima de la pelota
BALL_SPEED_MAX = 6  # Velocidad máxima de la pelota
BAR_WIDTH = 100  # Ancho de la barra
BAR_HEIGHT = 20  # Altura de la barra
BAR_SPEED = 15  # Velocidad de la barra
MAX_LIVES = 3  # Número máximo de vidas permitidas
BALL_RADIUS = 10  # Radio de la pelota


class Ball:
    """Clase que representa una pelota"""

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.dx = random.uniform(BALL_SPEED_MIN, BALL_SPEED_MAX) * random.choice([-1, 1])
        self.dy = random.uniform(BALL_SPEED_MIN, BALL_SPEED_MAX) * random.choice([-1, 1])

    def move(self):
        """Mueve la pelota según su velocidad"""
        self.x += self.dx
        self.y += self.dy


class MyGame(arcade.Window):
    """ Clase principal del juego """

    def __init__(self):
        """ Inicializador """
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Pelota, Barra, Rebotes, Puntuación y Nuevas Bolas")
        arcade.set_background_color(arcade.color.BLACK)

        # Inicializar la barra (posición inicial)
        self.bar_x = SCREEN_WIDTH // 2
        self.bar_y = BAR_HEIGHT * 2  # Altura desde la parte inferior de la ventana

        # Inicializar la pelota inicial
        self.balls = [Ball(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)]

        # Contador de vidas y puntuación
        self.lives = MAX_LIVES
        self.score = 0

        # Estado del juego
        self.game_over = False

        # Movimiento continuo de la barra (teclas presionadas)
        self.moving_left = False
        self.moving_right = False

    def on_draw(self):
        """ Método para dibujar todo en la ventana """
        self.clear()

        # Dibujar la barra
        arcade.draw_rectangle_filled(self.bar_x, self.bar_y, BAR_WIDTH, BAR_HEIGHT, arcade.color.WHITE)

        # Dibujar las pelotas
        for ball in self.balls:
            arcade.draw_circle_filled(ball.x, ball.y, BALL_RADIUS, arcade.color.RED)

        # Dibujar las vidas restantes y puntuación
        arcade.draw_text(f"Vidas: {self.lives}", 10, SCREEN_HEIGHT - 30, arcade.color.WHITE, 16)
        arcade.draw_text(f"Puntuación: {self.score}", 10, SCREEN_HEIGHT - 60, arcade.color.WHITE, 16)

        # Si el juego termina, mostrar mensaje
        if self.game_over:
            arcade.draw_text("¡Pulsa ESPACIO para reiniciar!", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
                             arcade.color.YELLOW, 20, anchor_x="center")

    def on_update(self, delta_time):
        """ Lógica del juego: movimiento y colisiones """
        if self.game_over:
            return

        # Movimiento continuo de la barra
        if self.moving_left:
            self.bar_x -= BAR_SPEED
            if self.bar_x - BAR_WIDTH / 2 < 0:  # Evitar salir por el lado izquierdo
                self.bar_x = BAR_WIDTH / 2
        if self.moving_right:
            self.bar_x += BAR_SPEED
            if self.bar_x + BAR_WIDTH / 2 > SCREEN_WIDTH:  # Evitar salir por el lado derecho
                self.bar_x = SCREEN_WIDTH - BAR_WIDTH / 2

        # Lista de pelotas que deben ser eliminadas
        balls_to_remove = []

        # Gestionar las pelotas
        for ball in self.balls:
            ball.move()

            # Detectar colisiones con los bordes de la ventana
            if ball.x <= 0 or ball.x >= SCREEN_WIDTH:  # Rebote en los bordes laterales
                ball.dx *= -1
            if ball.y >= SCREEN_HEIGHT:  # Rebote en el borde superior
                ball.dy *= -1
            if ball.y <= 0:  # La pelota toca el borde inferior
                self.lives -= 1
                balls_to_remove.append(ball)  # Marcar para eliminar
                continue

            # Detectar colisión de la pelota con la barra
            if (self.bar_y - BAR_HEIGHT / 2 <= ball.y - BALL_RADIUS <= self.bar_y + BAR_HEIGHT / 2) and \
                    (self.bar_x - BAR_WIDTH / 2 <= ball.x <= self.bar_x + BAR_WIDTH / 2):
                ball.dy = abs(ball.dy)  # Asegurar que la pelota rebote hacia arriba
                ball.dx += random.uniform(-1, 1)  # Variar ligeramente la dirección horizontal
                self.score += 1  # Incrementar la puntuación
                # Añadir una pelota cada 10 puntos
                if self.score % 10 == 0:
                    self.add_new_ball()

        # Eliminar las pelotas marcadas
        for ball in balls_to_remove:
            self.balls.remove(ball)

        # Si no quedan pelotas, finalizar el juego
        if not self.balls and self.lives > 0:
            self.add_new_ball()
        elif not self.balls and self.lives <= 0:
            self.game_over = True

    def add_new_ball(self):
        """Añade una nueva pelota al juego"""
        new_ball = Ball(self.bar_x, self.bar_y + 50)  # Nueva pelota cerca de la barra
        self.balls.append(new_ball)

    def on_key_press(self, key, modifiers):
        """ Manejar entrada de teclado para mover la barra y reiniciar el juego """
        if key == arcade.key.LEFT:
            self.moving_left = True  # Iniciar movimiento continuo hacia la izquierda
        elif key == arcade.key.RIGHT:
            self.moving_right = True  # Iniciar movimiento continuo hacia la derecha

        # Reiniciar juego si la partida terminó
        elif key == arcade.key.SPACE and self.game_over:
            self.reset_game()

    def on_key_release(self, key, modifiers):
        """ Detener el movimiento continuo cuando se suelta una tecla """
        if key == arcade.key.LEFT:
            self.moving_left = False
        elif key == arcade.key.RIGHT:
            self.moving_right = False

    def reset_game(self):
        """ Reiniciar el estado del juego """
        self.lives = MAX_LIVES
        self.score = 0
        self.balls = [Ball(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)]
        self.bar_x = SCREEN_WIDTH // 2
        self.game_over = False


def main():
    """ Método principal """
    window = MyGame()
    arcade.run()


main()
