import arcade
import random

# --- Constants ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
TRIANGLE_SIZE = 20
CIRCLE_RADIUS = 15
COIN_RADIUS = 10
CIRCLE_SPEED = 2
NUM_CIRCLES = 10
NUM_COINS = 10
SAFE_DISTANCE = 100

# --- Paths to images ---
NAVE_IMAGE = "C:\\Users\\diego\\OneDrive\\Escritorio\\universidad\\videojuegos\\sprites\\asteroids\\nave.png"
METEORITO_IMAGE = "C:\\Users\\diego\\OneDrive\\Escritorio\\universidad\\videojuegos\\sprites\\asteroids\\meteorito.png"
MONEDA_IMAGE = "C:\\Users\\diego\\OneDrive\\Escritorio\\universidad\\videojuegos\\sprites\\asteroids\\monedas.png"

class Meteorito:
    """Clase que representa los meteoritos en el juego."""
    def __init__(self, speed):
        self.x = random.randint(0, SCREEN_WIDTH)
        self.y = random.randint(0, SCREEN_HEIGHT)
        self.dx = random.choice([-speed, speed])
        self.dy = random.choice([-speed, speed])
        self.sprite = arcade.Sprite(METEORITO_IMAGE, scale=0.5)  # Aumentado el tamaño del meteorito
        self.sprite.center_x = self.x
        self.sprite.center_y = self.y

    def update(self):
        """Actualiza la posición del meteorito."""
        self.x += self.dx
        self.y += self.dy
        if self.x < 0 or self.x > SCREEN_WIDTH:
            self.dx *= -1
        if self.y < 0 or self.y > SCREEN_HEIGHT:
            self.dy *= -1
        self.sprite.center_x = self.x
        self.sprite.center_y = self.y

    def draw(self):
        """Dibuja el meteorito en la pantalla."""
        self.sprite.draw()

class Moneda:
    """Clase que representa las monedas en el juego."""
    def __init__(self):
        self.x = random.randint(0, SCREEN_WIDTH)
        self.y = random.randint(0, SCREEN_HEIGHT)
        self.sprite = arcade.Sprite(MONEDA_IMAGE, scale=0.5)  # Aumentado el tamaño de la moneda
        self.sprite.center_x = self.x
        self.sprite.center_y = self.y

    def relocate(self):
        """Reubica la moneda en una nueva posición aleatoria."""
        self.x = random.randint(0, SCREEN_WIDTH)
        self.y = random.randint(0, SCREEN_HEIGHT)
        self.sprite.center_x = self.x
        self.sprite.center_y = self.y

    def draw(self):
        """Dibuja la moneda en la pantalla."""
        self.sprite.draw()

class MyGame(arcade.Window):
    """Clase principal del juego."""
    def __init__(self):
        """Inicializador"""
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Nave Dodge Game")
        self.nave_x = SCREEN_WIDTH // 2
        self.nave_y = SCREEN_HEIGHT // 2
        self.meteoritos = [Meteorito(CIRCLE_SPEED) for _ in range(NUM_CIRCLES)]
        self.monedas = [Moneda() for _ in range(NUM_COINS)]
        self.score = 0
        self.game_over = False
        self.nave_sprite = arcade.Sprite(NAVE_IMAGE, scale=0.5)  # Aumentado el tamaño de la nave
        self.nave_sprite.center_x = self.nave_x
        self.nave_sprite.center_y = self.nave_y
        self.set_mouse_visible(False)  # Oculta el ratón

    def on_draw(self):
        """Dibuja todos los elementos en la pantalla."""
        self.clear()
        if self.game_over:
            arcade.draw_text("Game Over!", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 30,
                             arcade.color.WHITE, 24, anchor_x="center")
            arcade.draw_text(f"Score: {self.score}", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2,
                             arcade.color.WHITE, 24, anchor_x="center")
            arcade.draw_text("Press SPACE to restart", SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 30,
                             arcade.color.WHITE, 14, anchor_x="center")
        else:
            self.nave_sprite.draw()
            for meteorito in self.meteoritos:
                meteorito.draw()
            for moneda in self.monedas:
                moneda.draw()
            arcade.draw_text(f"Score: {self.score}", 10, 10, arcade.color.WHITE, 14)

    def on_update(self, delta_time):
        """Actualiza la lógica del juego."""
        if not self.game_over:
            for meteorito in self.meteoritos:
                meteorito.update()
                if self.check_collision(meteorito.x, meteorito.y, CIRCLE_RADIUS):
                    self.game_over = True

            for moneda in self.monedas:
                if self.check_collision(moneda.x, moneda.y, COIN_RADIUS):
                    moneda.relocate()
                    self.score += 1
                    if self.score % 3 == 0:
                        self.increase_difficulty()

            self.nave_sprite.center_x = self.nave_x
            self.nave_sprite.center_y = self.nave_y

    def check_collision(self, x, y, radius):
        """Comprueba si hay colisión entre la nave y otro objeto."""
        return (self.nave_x - x) ** 2 + (self.nave_y - y) ** 2 < (TRIANGLE_SIZE + radius) ** 2

    def on_mouse_motion(self, x, y, dx, dy):
        """Actualiza la posición de la nave según el movimiento del ratón."""
        if not self.game_over:
            self.nave_x = x
            self.nave_y = y

    def on_key_press(self, key, modifiers):
        """Reinicia el juego si se presiona la tecla SPACE."""
        if key == arcade.key.SPACE and self.game_over:
            self.reset_game()

    def reset_game(self):
        """Reinicia el juego."""
        self.nave_x = SCREEN_WIDTH // 2
        self.nave_y = SCREEN_HEIGHT // 2
        self.meteoritos = [Meteorito(CIRCLE_SPEED) for _ in range(NUM_CIRCLES)]
        self.monedas = [Moneda() for _ in range(NUM_COINS)]
        self.score = 0
        self.game_over = False
        self.ensure_safe_start()

    def ensure_safe_start(self):
        """Asegura que la nave no tenga ningún meteorito cerca al inicio del juego."""
        for meteorito in self.meteoritos:
            while self.check_collision(meteorito.x, meteorito.y, SAFE_DISTANCE):
                meteorito.x = random.randint(0, SCREEN_WIDTH)
                meteorito.y = random.randint(0, SCREEN_HEIGHT)

    def increase_difficulty(self):
        """Aumenta la dificultad del juego añadiendo más meteoritos y aumentando su velocidad."""
        new_speed = CIRCLE_SPEED + self.score // 3
        self.meteoritos.append(Meteorito(new_speed))

def main():
    """Función principal que inicia el juego."""
    window = MyGame()
    arcade.run()

main()
