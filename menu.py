from palabraAbyte import palabraAbyte
from operacion import caracterbyte

def main():
  while True:
      print("Menú:")
      print("1. Obtener representación en byte de un carácter")
      print("2. Obtener representación en byte de una palabra")
      print("0. Salir")

      opcion = input("Ingrese su opción (0-2): ")

      if opcion == '1':
        caracterbyte()
      elif opcion == '2':
        palabraAbyte()
      elif opcion == 0:
        return False
      else:
        print("opcion no valida")
        
        
if __name__ == "__main__":
  main()
