def obtener_representacion_byte(caracter):
  representacion_byte = ' '.join(format(b, '08b') for b in caracter.encode())
  return representacion_byte

def main():
  while True:
      print("Menú:")
      print("1. Obtener representación en byte de un carácter")
      print("2. Obtener representación en byte de una palabra")
      print("0. Salir")

      opcion = input("Ingrese su opción (0-2): ")

      if opcion == '1':
          caracter = input("Ingrese un carácter: ")
          resultado = obtener_representacion_byte(caracter)
          print(f"Representación en byte de '{caracter}': {resultado}")
      
if __name__ == "__main__":
  main()
