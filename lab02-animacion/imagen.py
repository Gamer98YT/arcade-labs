
import arcade

def dibujar_tractor(x, y):
    """
    Dibuja un tractor con humo en las coordenadas (x, y).
    El punto (x, y) corresponde al centro de la rueda trasera grande.
    """
    # --- Tractor Body ---
    # Motor
    arcade.draw_rect_filled(arcade.XYWH(x + 110, y + 10, 140, 70), arcade.color.GRAY)
    arcade.draw_rect_filled(arcade.XYWH(x + 100, y - 5, 90, 40), arcade.color.BLACK)
    # Chimenea (tubo de escape)
    # El centro de la chimenea está en (x+90, y+65). La altura es 40.
    # La punta superior de la chimenea está en y + 65 + 20 = y + 85.
    arcade.draw_rect_filled(arcade.XYWH(x + 90, y + 65, 10, 40), arcade.color.BLACK)

    # --- Wheels ---
    # Rueda Trasera (Ancla x, y)
    arcade.draw_circle_filled(x, y, 50, arcade.color.BLACK)
    arcade.draw_circle_filled(x, y, 45, arcade.color.BLACK_OLIVE)
    arcade.draw_circle_filled(x, y, 35, arcade.color.OLD_LACE)
    arcade.draw_circle_filled(x, y, 10, arcade.color.RED)
    # Rueda Delantera
    arcade.draw_circle_filled(x + 160, y - 20, 30, arcade.color.BLACK)
    arcade.draw_circle_filled(x + 160, y - 20, 25, arcade.color.BLACK_OLIVE)
    arcade.draw_circle_filled(x + 160, y - 20, 18, arcade.color.OLD_LACE)
    arcade.draw_circle_filled(x + 160, y - 20, 5, arcade.color.RED)

    # --- Humo (Smoke) ---
    # Dibujamos el humo AL FINAL para que aparezca por encima del tractor.
    # Usamos colores RGBA (Rojo, Verde, Azul, Alfa/Transparencia).
    # Alfa 255 es sólido, 0 es invisible.

    smoke_base_x = x + 90
    smoke_base_y = y + 85 # Justo encima del tubo

    # Nube 1: Pequeña, oscura, cerca de la salida
    arcade.draw_circle_filled(smoke_base_x, smoke_base_y + 5, 8, (100, 100, 100, 200))

    # Nube 2: Mediana, gris medio, un poco más arriba y a la derecha
    arcade.draw_circle_filled(smoke_base_x + 5, smoke_base_y + 20, 12, (150, 150, 150, 150))

    # Nube 3: Grande, gris claro, muy transparente, más arriba
    arcade.draw_circle_filled(smoke_base_x + 12, smoke_base_y + 38, 16, (200, 200, 200, 100))

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