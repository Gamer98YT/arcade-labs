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

visualizar_preguntas("lab03-preguntas/preguntas.txt")