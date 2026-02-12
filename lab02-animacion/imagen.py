
import arcade

def dibujar_tractor(x, y):
    """
    Dibuja un tractor en las coordenadas (x, y).
    El punto (x, y) corresponde al centro de la rueda trasera grande.
    """
    
    # --- Draw the engine ---
    # Original: 600 (x+110), 120 (y+10)
    arcade.draw_rect_filled(arcade.XYWH(x + 110, y + 10, 140, 70), arcade.color.GRAY)
    # Original: 590 (x+100), 105 (y-5)
    arcade.draw_rect_filled(arcade.XYWH(x + 100, y - 5, 90, 40), arcade.color.BLACK)

    # --- Draw the smoke stack ---
    # Original: 580 (x+90), 175 (y+65)
    arcade.draw_rect_filled(arcade.XYWH(x + 90, y + 65, 10, 40), arcade.color.BLACK)

    # --- Back wheel ---
    # Esta es nuestra ancla (x, y)
    arcade.draw_circle_filled(x, y, 50, arcade.color.BLACK)
    arcade.draw_circle_filled(x, y, 45, arcade.color.BLACK_OLIVE)
    arcade.draw_circle_filled(x, y, 35, arcade.color.OLD_LACE)
    arcade.draw_circle_filled(x, y, 10, arcade.color.RED)

    # --- Front wheel ---
    # Original: 650 (x+160), 90 (y-20)
    fx = x + 160
    fy = y - 20
    arcade.draw_circle_filled(fx, fy, 30, arcade.color.BLACK)
    arcade.draw_circle_filled(fx, fy, 25, arcade.color.BLACK_OLIVE)
    arcade.draw_circle_filled(fx, fy, 18, arcade.color.OLD_LACE)
    arcade.draw_circle_filled(fx, fy, 5, arcade.color.RED)

arcade.open_window(800, 600, "Dibujo fragger")

# Color de fondo
arcade.set_background_color(arcade.color.AIR_SUPERIORITY_BLUE)
arcade.start_render()

# Asfalto
arcade.draw_lrbt_rectangle_filled(0, 800, 0, 200, (30, 31, 33))

# -Dibujo de la carretera-

# Linea superior de la carretera
arcade.draw_lrbt_rectangle_filled(0, 800, 150, 160, arcade.color.WHITE)

# Linea inferior de la carretera
arcade.draw_lrbt_rectangle_filled(0, 800, 50, 60, arcade.color.WHITE)

# Lineas discontinuas del medio de la carretera
arcade.draw_lrbt_rectangle_filled(0, 100, 100, 110, arcade.color.WHITE)
arcade.draw_lrbt_rectangle_filled(120, 220, 100, 110, arcade.color.WHITE)
arcade.draw_lrbt_rectangle_filled(240, 340, 100, 110, arcade.color.WHITE)
arcade.draw_lrbt_rectangle_filled(360, 460, 100, 110, arcade.color.WHITE)
arcade.draw_lrbt_rectangle_filled(480, 580, 100, 110, arcade.color.WHITE)
arcade.draw_lrbt_rectangle_filled(600, 700, 100, 110, arcade.color.WHITE)
arcade.draw_lrbt_rectangle_filled(720, 820, 100, 110, arcade.color.WHITE)

# --- Draw the tractor ---

dibujar_tractor(100, 110)

# Draw the engine
arcade.draw_rect_filled(arcade.XYWH(600, 120, 140, 70), arcade.color.GRAY)
arcade.draw_rect_filled(arcade.XYWH(590, 105, 90, 40), arcade.color.BLACK)

# Draw the smoke stack
arcade.draw_rect_filled(arcade.XYWH(580, 175, 10, 40), arcade.color.BLACK)

# Back wheel
arcade.draw_circle_filled(490, 110, 50, arcade.color.BLACK)
arcade.draw_circle_filled(490, 110, 45, arcade.color.BLACK_OLIVE)
arcade.draw_circle_filled(490, 110, 35, arcade.color.OLD_LACE)
arcade.draw_circle_filled(490, 110, 10, arcade.color.RED)

# Front wheel
arcade.draw_circle_filled(650, 90, 30, arcade.color.BLACK)
arcade.draw_circle_filled(650, 90, 25, arcade.color.BLACK_OLIVE)
arcade.draw_circle_filled(650, 90, 18, arcade.color.OLD_LACE)
arcade.draw_circle_filled(650, 90, 5, arcade.color.RED)

# --- Finish drawing ---

# Keep the window up until someone closes it.
arcade.finish_render()
arcade.run()