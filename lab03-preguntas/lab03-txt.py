def visualizar_preguntas(nombre_archivo):
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            for numero_pregunta, linea in enumerate(archivo, start=1):
                linea = linea.strip()
                datos = linea.split('|')
                if len(datos) > 1:
                    pregunta = datos[0]
                    opciones = datos[1:]
                    print(f"Pregunta {numero_pregunta}: {pregunta}")
                    for i, opcion in enumerate(opciones, start=1):
                        print(f" {i}) {opcion}")
                    print("-" * 50)
                else:
                    print(f"Error en la linea {numero_pregunta}: formato incorrecto.")
    except FileNotFoundError:
        print(f"Error: El archivo {nombre_archivo} no se ha encontrado.")



def extraer_pregunta(pregunta: str) -> dict:
    try:

        partes = pregunta.split('|')
        
        if len(partes) != 3:
            raise ValueError("El formato debe ser: 'Pregunta | Correcta | Opcion1, Opcion2...'")
            
        pregunta = partes[0].strip()
        correcta = partes[1].strip()
        
        opciones_crudas = partes[2].split(',')
        opciones = [opcion.strip() for opcion in opciones_crudas]
        
        return {
            "pregunta": pregunta,
            "correcta": correcta,
            "opciones": opciones
        }
        
    except Exception as e:
        print(f"Error al procesar la pregunta: {e}")
        return {}


def visualizar_preguntas_una_a_una(nombre_archivo):
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            for numero_pregunta, linea in enumerate(archivo, start=1):
                linea = linea.strip() 

                datos = extraer_pregunta(linea)
                
                if datos:
                    print(f"\n=== Pregunta {numero_pregunta} ===")
                    print(datos["pregunta"])
                    print("-" * 30)
                    

                    for i, opcion in enumerate(datos["opciones"], start=1):
                        print(f" {i}) {opcion}")
                    
                    print("-" * 30)

                    input("Presiona [Enter] para continuar con la siguiente pregunta...")
                    
                else:
                    print(f"Error en la linea {numero_pregunta}: formato incorrecto. Saltando...")
                    
        print("\n¡Has llegado al final de las preguntas!")
                    
    except FileNotFoundError:
        print(f"Error: El archivo '{nombre_archivo}' no se ha encontrado.")

def jugar_preguntas(nombre_archivo):
    puntuacion = 0 
    
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            for numero_pregunta, linea in enumerate(archivo, start=1):
                linea = linea.strip()
                
                if not linea:
                    continue 

                datos = extraer_pregunta(linea)
                
                if datos:
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
                    
                else:
                    print(f"Error en la linea {numero_pregunta}: formato incorrecto. Omitiendo la linea.")
                    
        print("\n" + "=" * 30)
        print(f"¡Juego terminado! Tu puntuación final es: {puntuacion} puntos.")
        print("=" * 30)
                    
    except FileNotFoundError:
        print(f"Error: El archivo '{nombre_archivo}' no se ha encontrado.")

jugar_preguntas("lab03-preguntas/preguntas.txt")