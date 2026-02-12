
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

def dibujar_coche_deportivo(x, y):
    """
    Dibuja un coche deportivo rojo en (x, y).
    (x, y) es el centro de la rueda trasera.
    """
    
    # --- Carrocería (Chassis) ---
    # Cuerpo principal (largo y bajo)
    # x + 85 es el centro del cuerpo respecto a la rueda trasera
    arcade.draw_rect_filled(arcade.XYWH(x + 85, y + 15, 230, 45), arcade.color.CRIMSON)
    
    # Cabina (Parte superior)
    arcade.draw_rect_filled(arcade.XYWH(x + 70, y + 50, 110, 35), arcade.color.CRIMSON)
    
    # Ventana (Cristal)
    arcade.draw_rect_filled(arcade.XYWH(x + 75, y + 50, 80, 25), arcade.color.SKY_BLUE)

    # --- Detalles Deportivos ---
    # Alerón trasero (Spoiler)
    # Soporte del alerón
    arcade.draw_rect_filled(arcade.XYWH(x - 20, y + 35, 10, 25), arcade.color.CRIMSON)
    # El ala del alerón
    arcade.draw_rect_filled(arcade.XYWH(x - 20, y + 50, 40, 10), arcade.color.DARK_RED)

    # Faro delantero (Amarillo)
    arcade.draw_rect_filled(arcade.XYWH(x + 190, y + 20, 10, 15), arcade.color.YELLOW)
    
    # Luz trasera (Roja brillante)
    arcade.draw_rect_filled(arcade.XYWH(x - 25, y + 20, 10, 15), arcade.color.RED)

    # --- Ruedas ---
    # Rueda Trasera (Nuestro punto de ancla X, Y)
    arcade.draw_circle_filled(x, y, 28, arcade.color.BLACK)       # Neumático
    arcade.draw_circle_filled(x, y, 18, arcade.color.SILVER)      # Llanta

    # Rueda Delantera (Separada 170 píxeles)
    front_wheel_x = x + 170
    arcade.draw_circle_filled(front_wheel_x, y, 28, arcade.color.BLACK)
    arcade.draw_circle_filled(front_wheel_x, y, 18, arcade.color.SILVER)

def dibujar_coche_invertido(x, y):
    """
    Dibuja un coche azul mirando hacia la IZQUIERDA.
    (x, y) es el centro de la rueda trasera (la de la derecha).
    """
    # --- Carrocería ---
    # Cuerpo principal (Bloque grande hacia la izquierda)
    # x - 85 es el centro del rectángulo para que crezca hacia la izquierda
    arcade.draw_rect_filled(arcade.XYWH(x - 85, y + 20, 240, 45), arcade.color.DODGER_BLUE)

    # Techo / Cabina (Más cuadrado que el deportivo rojo)
    arcade.draw_rect_filled(arcade.XYWH(x - 50, y + 55, 100, 30), arcade.color.DODGER_BLUE)
    
    # Ventana (Cristal oscuro)
    arcade.draw_rect_filled(arcade.XYWH(x - 50, y + 55, 80, 20), arcade.color.BLACK)

    # --- Detalles ---
    # Franja de carreras blanca horizontal
    arcade.draw_rect_filled(arcade.XYWH(x - 85, y + 30, 240, 10), arcade.color.WHITE)

    # Alerón trasero (En el lado derecho, x positivo relativo al centro del cuerpo)
    arcade.draw_rect_filled(arcade.XYWH(x + 25, y + 45, 15, 20), arcade.color.DODGER_BLUE) # Soporte
    arcade.draw_rect_filled(arcade.XYWH(x + 25, y + 55, 40, 10), arcade.color.MIDNIGHT_BLUE) # Ala

    # Faro delantero (Amarillo, en el extremo IZQUIERDO)
    arcade.draw_rect_filled(arcade.XYWH(x - 200, y + 20, 15, 15), arcade.color.YELLOW)
    
    # Luz trasera (Roja, en el extremo DERECHO)
    arcade.draw_rect_filled(arcade.XYWH(x + 30, y + 25, 10, 25), arcade.color.RED)

    # --- Ruedas ---
    # Rueda Trasera (Ancla X, Y - Derecha)
    arcade.draw_circle_filled(x, y, 30, arcade.color.BLACK)       # Neumático
    arcade.draw_circle_filled(x, y, 20, arcade.color.GOLD)        # Llanta dorada

    # Rueda Delantera (Hacia la IZQUIERDA, restamos X)
    front_wheel_x = x - 170
    arcade.draw_circle_filled(front_wheel_x, y, 30, arcade.color.BLACK)
    arcade.draw_circle_filled(front_wheel_x, y, 20, arcade.color.GOLD)







arcade.open_window(800, 600, "Dibujo fragger")

# Color de fondo
arcade.set_background_color(arcade.color.AIR_SUPERIORITY_BLUE)
arcade.start_render()

# Asfalto y hierba de alrededor
arcade.draw_lrbt_rectangle_filled(0, 800, 0, 200, (30, 31, 33))
arcade.draw_lrbt_rectangle_filled(0, 800, 0, 50, arcade.color.BITTER_LIME)
arcade.draw_lrbt_rectangle_filled(0, 800, 160, 200, arcade.color.BITTER_LIME)

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

# --- Objetos ---

dibujar_tractor(100, 110)
dibujar_coche_invertido(700, 150)
dibujar_coche_deportivo(400, 90)



# --- Fin del dibujo ---

# Mantener ventana abierta hasta que el usuario la cierre
arcade.finish_render()
arcade.run()