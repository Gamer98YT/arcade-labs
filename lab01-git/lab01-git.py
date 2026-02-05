import arcade

WIDTH = 800
HEIGHT = 600
print("Yo tambien soy un conflicto")

arcade.open_window(WIDTH, HEIGHT, "Example")

arcade.start_render()
arcade.draw_text("Hello, world", 350, 300, arcade.color.WHITE)
arcade.finish_render()
print("Se fue el conflicto")

arcade.run()
