import arcade

# --- Configuración de la Pantalla ---
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Animación Carretera"

# Velocidades
VELOCIDAD_TRACTOR = 3
VELOCIDAD_COCHE = 5

# --- FUNCIONES DE DIBUJO ---

def dibujar_escenario():
    """ 
    Dibuja la carretera usando draw_lrbt_rectangle_filled 
    Orden de parámetros: (Izquierda, Derecha, ABAJO, ARRIBA)
    """
    # 1. Base oscura (Asfalto/Tierra) - De y=0 a y=200
    arcade.draw_lrbt_rectangle_filled(0, 800, 0, 200, (30, 31, 33))

    # 2. Césped inferior - De y=0 a y=50
    arcade.draw_lrbt_rectangle_filled(0, 800, 0, 50, arcade.color.BITTER_LIME)

    # 3. Césped superior - De y=160 a y=200
    arcade.draw_lrbt_rectangle_filled(0, 800, 160, 200, arcade.color.BITTER_LIME)

    # 4. Línea Blanca Superior de la carretera - De y=150 a y=160
    arcade.draw_lrbt_rectangle_filled(0, 800, 150, 160, arcade.color.WHITE)

    # 5. Línea Blanca Inferior de la carretera - De y=50 a y=60
    arcade.draw_lrbt_rectangle_filled(0, 800, 50, 60, arcade.color.WHITE)

    # 6. Líneas discontinuas centrales - Altura entre 100 y 110
    for x in range(0, 800, 120): 
        arcade.draw_lrbt_rectangle_filled(x, x + 100, 100, 110, arcade.color.WHITE)

def dibujar_tractor(x, y):
    """ Dibuja el tractor en (x, y) """
    # Motor
    arcade.draw_rect_filled(arcade.XYWH(x + 110, y + 10, 140, 70), arcade.color.GRAY)
    arcade.draw_rect_filled(arcade.XYWH(x + 100, y - 5, 90, 40), arcade.color.BLACK)
    # Chimenea
    arcade.draw_rect_filled(arcade.XYWH(x + 90, y + 65, 10, 40), arcade.color.BLACK)
    
    # Rueda Trasera
    arcade.draw_circle_filled(x, y, 50, arcade.color.BLACK)
    arcade.draw_circle_filled(x, y, 45, arcade.color.BLACK_OLIVE)
    arcade.draw_circle_filled(x, y, 35, arcade.color.OLD_LACE)
    arcade.draw_circle_filled(x, y, 10, arcade.color.RED)
    
    # Rueda Delantera
    arcade.draw_circle_filled(x + 160, y - 20, 30, arcade.color.BLACK)
    arcade.draw_circle_filled(x + 160, y - 20, 25, arcade.color.BLACK_OLIVE)
    arcade.draw_circle_filled(x + 160, y - 20, 18, arcade.color.OLD_LACE)
    arcade.draw_circle_filled(x + 160, y - 20, 5, arcade.color.RED)

    # Humo
    sb_x = x + 90
    sb_y = y + 85
    arcade.draw_circle_filled(sb_x, sb_y + 5, 8, (100, 100, 100, 200))
    arcade.draw_circle_filled(sb_x + 5, sb_y + 20, 12, (150, 150, 150, 150))
    arcade.draw_circle_filled(sb_x + 12, sb_y + 38, 16, (200, 200, 200, 100))

def dibujar_coche_invertido(x, y):
    """ Dibuja el coche azul mirando a la izquierda """
    # Carrocería
    arcade.draw_rect_filled(arcade.XYWH(x - 85, y + 20, 240, 45), arcade.color.DODGER_BLUE)
    arcade.draw_rect_filled(arcade.XYWH(x - 50, y + 55, 100, 30), arcade.color.DODGER_BLUE)
    arcade.draw_rect_filled(arcade.XYWH(x - 50, y + 55, 80, 20), arcade.color.BLACK)
    # Detalles
    arcade.draw_rect_filled(arcade.XYWH(x - 85, y + 30, 240, 10), arcade.color.WHITE)
    arcade.draw_rect_filled(arcade.XYWH(x + 25, y + 45, 15, 20), arcade.color.DODGER_BLUE)
    arcade.draw_rect_filled(arcade.XYWH(x + 25, y + 55, 40, 10), arcade.color.MIDNIGHT_BLUE)
    arcade.draw_rect_filled(arcade.XYWH(x - 200, y + 20, 15, 15), arcade.color.YELLOW)
    arcade.draw_rect_filled(arcade.XYWH(x + 30, y + 25, 10, 25), arcade.color.RED)
    # Ruedas
    arcade.draw_circle_filled(x, y, 30, arcade.color.BLACK)
    arcade.draw_circle_filled(x, y, 20, arcade.color.GOLD)
    front_wheel_x = x - 170
    arcade.draw_circle_filled(front_wheel_x, y, 30, arcade.color.BLACK)
    arcade.draw_circle_filled(front_wheel_x, y, 20, arcade.color.GOLD)

# --- CLASE DEL JUEGO ---

class MiJuego(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.AIR_SUPERIORITY_BLUE)

        # Posiciones iniciales
        self.tractor_x = -100      
        self.tractor_y = 115        
        self.coche_azul_x = 900    
        self.coche_azul_y = 150    

    def on_draw(self):
        """ Renderizado """
        self.clear() # Limpiar pantalla

        dibujar_escenario()
        dibujar_coche_invertido(self.coche_azul_x, self.coche_azul_y)
        dibujar_tractor(self.tractor_x, self.tractor_y)


    def on_update(self, delta_time):
        """ Movimiento """
        # Mover Tractor a la derecha
        self.tractor_x += VELOCIDAD_TRACTOR
        if self.tractor_x > SCREEN_WIDTH + 150:
            self.tractor_x = -200

        # Mover Coche Azul a la izquierda
        self.coche_azul_x -= VELOCIDAD_COCHE
        if self.coche_azul_x < -250:
            self.coche_azul_x = SCREEN_WIDTH + 100

def main():
    window = MiJuego(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()

if __name__ == "__main__":
    main()