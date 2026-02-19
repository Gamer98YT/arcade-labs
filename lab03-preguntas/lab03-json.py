import json

def jugar_preguntas_json(nombre_archivo):
    puntuacion = 0
    
    try:

        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            lista_preguntas = json.load(archivo)
            
        for numero_pregunta, datos in enumerate(lista_preguntas, start=1):
            
            print(f"\n=== Pregunta {numero_pregunta} ===")
            print(datos["pregunta"])
            print("-" * 30)
            
            for i, opcion in enumerate(datos["opciones"], start=1):
                print(f" {i}) {opcion}")
            
            print("-" * 30)
            
            opcion_elegida = ""
            while True:
                respuesta_input = input("Elige el número de tu respuesta: ")
                
                if respuesta_input.isdigit():
                    indice_elegido = int(respuesta_input) - 1
                    if 0 <= indice_elegido < len(datos["opciones"]):
                        opcion_elegida = datos["opciones"][indice_elegido]
                        break 
                
                print("Entrada no válida. Por favor, introduce el número de una de las opciones.")
            
            if opcion_elegida == datos["correcta"]:
                puntuacion += 5
                print("¡Correcto! Sumas 5 puntos.")
            else:
                puntuacion -= 5
                print(f"¡Incorrecto! La respuesta correcta era: {datos['correcta']}. Pierdes 5 puntos.")
            
            print(f"Puntuación actual: {puntuacion} puntos")
                
        print("\n" + "=" * 30)
        print(f"¡Juego terminado! Tu puntuación final es: {puntuacion} puntos.")
        print("=" * 30)
                    
    except FileNotFoundError:
        print(f"Error: El archivo '{nombre_archivo}' no se ha encontrado.")
    except json.JSONDecodeError:
        print(f"Error: El archivo '{nombre_archivo}' no tiene un formato JSON válido. Revisa las comillas y comas.")


jugar_preguntas_json("lab03-preguntas/preguntas.json")