"""
Actividad n°6 "Manejo de archivos con Python"
Nicolás Jofré Andrade

- Crear un archivo registro_notas.txt con:
    - Juan 85
    - Ana 92
    - Carlos 78
    - Maria 90
- Crea un archivo llamado manejo_archivos.py que lea registro_notas.txt y calcule el
promedio de las notas y escriba en un nuevo archivo promedio_notas.txt los resultados.
"""
def leer_archivo():

    try:
        with open("registro_notas.txt", "r") as archivo:
            contenido = archivo.read()
            print(contenido)
    except FileNotFoundError:
        print("El archivo no se ha encontrado.")
    except Exception as e:
        print("Error:", e)

def calcular_promedio():

  notas = []

  try:
    with open("registro_notas.txt", "r") as archivo:
      for linea in archivo:
        nombre, nota = linea.split()
        try:
          nota = int(nota)
        except ValueError:
          print(f"Error al convertir la nota '{nota}' para el estudiante '{nombre}'.")
          continue
        notas.append(nota)
  except FileNotFoundError:
    print("El archivo registro_notas.txt no se ha encontrado.")
    return
  except Exception as e:
    print("Error al leer el archivo:", e)
    return

  if not notas:
    print("No hay notas para calcular el promedio.")
    return

  promedio = sum(notas) / len(notas)

  try:
    with open("promedio_notas.txt", "w") as archivo:
      archivo.write(f"El promedio de las notas es: {promedio}")
      print("Se guardó en promedio_notas.txt correctamente!\n")
  except Exception as e:
    print("Error al escribir el archivo:", e)

# Menú de programa
while True:
    print("Menu: \n \t 1.Leer archivo \n \t 2.Calcular Promedio \n \t 3.Salir\n")
    opcion = int(input("Ingrese una opción del menú: \n"))

    if opcion == 1:
        leer_archivo()
    elif opcion == 2:
        calcular_promedio()
    elif opcion == 3:
        print("Saliendo del programa...")
        break
    else: 
        print("ERROR: Opción incorrecta")
        