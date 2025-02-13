"""
This is a sample program to show how to draw using the Python programming
language and the Arcade library.
"""

# Import the "arcade" library
import arcade

# Open up a window.
# From the "arcade" library, use a function called "open_window"
# Set the window title to "Drawing Example"
# Set the and dimensions (width and height)
arcade.open_window(800, 600, "Drawing Example")

# Set the background color
arcade.set_background_color(arcade.color.AIR_SUPERIORITY_BLUE)

# Get ready to draw
arcade.start_render()

# Draw the beach
arcade.draw_lrtb_rectangle_filled(0, 800, 200, 0, arcade.color.SAND)
arcade.draw_lrtb_rectangle_filled(0, 800, 300, 200, arcade.color.BLUE_SAPPHIRE)

# Draw the sun
arcade.draw_circle_filled(100, 500, 50, arcade.color.YELLOW)

# Draw waves
wave_color = (102, 153, 200)
# This wave will be filled below it
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

# Use filled polygons to fill the space under the wave
filled_wave_points = [(0, 300)] + wave_points + [(800, 300), (800, 200), (0, 200)]
arcade.draw_polygon_filled(filled_wave_points, arcade.color.BLUE_SAPPHIRE)

# Draw the wave outline on top after filling
arcade.draw_line_strip(
    wave_points,
    color=arcade.color.BLUE_SAPPHIRE,
    line_width=3
)

arcade.draw_line_strip(
    [
        (0, 230),
        (100, 240),
        (200, 220),
        (300, 240),
        (400, 220),
        (500, 240),
        (600, 220),
        (700, 240),
        (800, 230)
    ],
    color=wave_color,
    line_width=3
)

arcade.draw_line_strip(
    [
        (0, 260),
        (100, 270),
        (200, 250),
        (300, 270),
        (400, 250),
        (500, 270),
        (600, 250),
        (700, 270),
        (800, 260)
    ],
    color=wave_color,
    line_width=3
)

# Draw clouds in the sky
# Cloud 1
arcade.draw_circle_filled(200, 500, 30, arcade.color.WHITE)
arcade.draw_circle_filled(230, 510, 40, arcade.color.WHITE)
arcade.draw_circle_filled(260, 500, 30, arcade.color.WHITE)

# Cloud 2
arcade.draw_circle_filled(500, 450, 30, arcade.color.WHITE)
arcade.draw_circle_filled(530, 460, 40, arcade.color.WHITE)
arcade.draw_circle_filled(560, 450, 30, arcade.color.WHITE)

# Cloud 3
arcade.draw_circle_filled(700, 550, 30, arcade.color.WHITE)
arcade.draw_circle_filled(730, 560, 40, arcade.color.WHITE)
arcade.draw_circle_filled(760, 550, 30, arcade.color.WHITE)

# Draw birds using a loop
bird_positions = [(600, 550), (650, 530), (700, 560), (620, 510), (680, 540)]
for x, y in bird_positions:
    arcade.draw_arc_outline(x, y, 40, 20, arcade.color.WHITE, 0, 90, 3)  # Left wing
    arcade.draw_arc_outline(x + 40, y, 40, 20, arcade.color.WHITE, 90, 180, 3)  # Right wing

# Add umbrellas
# Umbrella 1
arcade.draw_line(300, 200, 300, 250, arcade.color.BROWN, 4)  # Umbrella pole
arcade.draw_arc_filled(300, 250, 80, 40, arcade.color.RED, 0, 180)  # Semicircle
arcade.draw_circle_filled(300, 270, 5, arcade.color.RED)  # Small circle on top

# Umbrella 2
arcade.draw_line(500, 200, 500, 250, arcade.color.BROWN, 4)  # Umbrella pole
arcade.draw_arc_filled(500, 250, 80, 40, arcade.color.BLUE, 0, 180)  # Semicircle
arcade.draw_circle_filled(500, 270, 5, arcade.color.BLUE)  # Small circle on top

# Add towels
# Towel 1
arcade.draw_lrtb_rectangle_filled(350, 400, 190, 160, arcade.color.YELLOW_ORANGE)

# Towel 2
arcade.draw_lrtb_rectangle_filled(600, 650, 190, 160, arcade.color.BABY_BLUE)

# Draw persons

# Circle for the head
arcade.draw_circle_filled(150, 220, 10, arcade.color.BLACK)

# Body (vertical line)
arcade.draw_line(150, 210, 150, 180, arcade.color.BLACK, 2)

# Arms (slanted lines)
arcade.draw_line(150, 200, 140, 190, arcade.color.BLACK, 2)
arcade.draw_line(150, 200, 160, 190, arcade.color.BLACK, 2)

# Legs (slanted lines for walking pose)
arcade.draw_line(150, 180, 140, 160, arcade.color.BLACK, 2)  # Left leg
arcade.draw_line(150, 180, 160, 170, arcade.color.BLACK, 2)  # Right leg

# Draw a stickman 2
arcade.draw_circle_filled(400, 260, 10, arcade.color.BLACK)  # Head
arcade.draw_line(400, 250, 400, 230, arcade.color.BLACK, 2)  # Body
arcade.draw_line(400, 245, 390, 250, arcade.color.BLACK, 2)  # Left arm
arcade.draw_line(400, 245, 410, 250, arcade.color.BLACK, 2)  # Right arm

# Draw a stickman 3
arcade.draw_circle_filled(375, 175, 10, arcade.color.BLACK)  # Head
arcade.draw_line(365, 175, 335, 175, arcade.color.BLACK, 2)  # Body (horizontal)
# Legs spread horizontally
arcade.draw_line(335, 175, 320, 185, arcade.color.BLACK, 2)  # Left leg
arcade.draw_line(335, 175, 320, 165, arcade.color.BLACK, 2)  # Right leg
# Arms spread horizontally
arcade.draw_line(365, 175, 380, 185, arcade.color.BLACK, 2)  # Left arm
arcade.draw_line(365, 175, 380, 165, arcade.color.BLACK, 2)  # Right arm

# --- Finish drawing ---
arcade.finish_render()


# Keep the window up until someone closes it.
arcade.run()

