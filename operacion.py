def caracterbyte():
    caracter = str("Ingrese un caracter")
    valor_ascii = ord(caracter)
    representacion_byte = bin(valor_ascii)[2:]
    print(f"El carácter '{caracter}' en bytes es: {representacion_byte}")



