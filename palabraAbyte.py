palabra = input("Ingrese la palabra que desea cambiar a byte: ")

for letra in palabra:
    repreBits = format(ord(letra),'08b')
    print(f"{letra}: {repreBits}")