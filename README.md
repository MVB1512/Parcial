# Parcial
# DOCUMENTACIÓN PARTE PRÁCTICA PARCIAL FINAL
### En este blog se encontrarán las evidencias sobre la parte practica del parcial final.
---
Para hacer este repositorio se crearon varias ramas para las operaciones, una para el menú, una para la representación en byte de un carácter, una para la representación en byte de una palabra y por último una donde está el archivo de gitignore para la información de las exclusiones del repositorio.

-------
- Código Menú

![](https://i.imgur.com/ZBXJzsz.png)

El propósito del código es crear un menú interactivo que permite al usuario elegir entre dos opciones para obtener la representación en bytes de un carácter o una palabra.
1.  **def main**: esta define la función principal llamada main. 
2.  **while True** : Inicia un bucle infinito, lo que significa que el menú se mostrará continuamente hasta que el usuario decida salir.
3. **opcion = input("Ingrese su opción (0-2): ")**: esta variable solicita al usuario que ingrese una opción del menú y al ingresarla, esta función guarda la entrada en la variable opcion.
4.  El bloque del condicional **if** y **elif** evalúa la opción ingresada y realiza las siguientes acciones:
    
    -   Si *opcion* es '1', llama a la función **caracterbyte()**.
    -   Si *opcion* es '2', llama a la función **palabraAbyte()**.
    -   Si *opcion* es '0', devuelve **False**, lo que rompe el bucle y sale del programa.
    -  si esto no se cumple, la condición **else** imprime "opcion no valida".
5.  **if __name__ == "__main__":**: esto comprueba si el script se está ejecutando directamente. Si es así, ejecuta la función **main()**.
----
- Código representación de una palabra en byte

![](https://i.imgur.com/UXvpYkp.png)
- Output del código

![](https://i.imgur.com/Z2Ay7uu.jpg)

El propósito de este código es tomar una palabra ingresada por el usuario y mostrar la representación en byte de cada letra de la palabra ingresada.
El programa primero le pide al usuario la palabra que quiere cambiar a bytes, después el programa cambia los caracteres a bytes mediante la función ord(letra) y después utiliza la función format(..., '08b') para pasar los bytes a una cadena de 8 bits.
1.  **def palabraAbyte()**: esto define la función **palabraAbyte()**.
    
2.  **palabra = input("Ingrese la palabra que desea cambiar a byte: ")**: esta variable solicita al usuario que ingrese una palabra y al hacerlo, esta guarda la entrada en la variable **palabra**.
    
3.  **for letra in palabra:**: este *for* inicia un bucle que itera sobre cada letra en la palabra ingresada.
    
4.  **repreBits = format(ord(letra),'08b')**: Para cada letra, utiliza la función **ord()** para obtener el valor ASCII de la letra y luego utiliza la función **format()** para convertir ese valor en una representación binaria de 8 bits. La parte `**(:08b)** asegura que la representación binaria tenga al menos 8 dígitos, rellenando con ceros a la izquierda si es necesario. La representación en bits se guarda en la variable **repreBits**.
    
5.  **print(f"{letra}: {repreBits}")**: lo que hace el *print* aquí es imprimir la letra original y su representación en bits en la misma línea.
----
- Código representación de un carácter en byte 
![](https://i.imgur.com/0DwcsRa.png)

El propósito de este código es convertir un carácter ingresada por el usuario y mostrar la representación en byte del ingresado.
1.  **def caracterbyte():**: Define la función **caracterbyte()**.
    
2.  **caracter = str("Ingrese un caracter")**:  esta variable solicita al usuario que ingrese una carácter y al hacerlo, esta guarda la entrada en la variable **caracter**.
    
3.  **valor_ascii = ord(caracter)**: en esta variable se utiliza la función *ord()* para obtener el valor ASCII del carácter ingresado y lo guarda en la variable **valor_ascii**.
    
4.  **representacion_byte = bin(valor_ascii)[2:]**: esta variable convierte el valor ASCII a su representación binaria utilizando la función *bin()*. El resultado incluirá el prefijo "0b", y *[2:]* se utiliza para excluir este prefijo y obtener solo la representación binaria.
    
5.  **print(f"El carácter '{caracter}' en bytes es: {representacion_byte}")**:este *print* imprime el carácter original y su representación en bytes en la misma línea.
---
### GitIgnore
¿Para qué sirve el gitignore en un repositorio de git? 
- El archivo **.gitignore** en un repositorio de Git se utiliza para especificar archivos y directorios que se deben ignorar, es decir, que no deben ser rastreados por Git.
---
 En este archivo de gitignore que se realizó en el parcial nos sirvió para agregar la información sobre la exclusión de aquellos archivos del repositorio que deseábamos que ignorara a la hora de ejecutarlo.
![](https://i.imgur.com/dGsXzq8.jpg)
![](https://i.imgur.com/u4u3nb6.jpg)

al crear el archivo en git bash, las exclusiones del repositorio son las siguientes:
![](https://i.imgur.com/Tf0r7RY.png)

Algunos de los comandos utilizados en este Git bash son los siguientes: 
-   **cd:** nos permite cambiarnos de carpeta, p.ej.  **cd** _NuevaCarpeta._
- **dir** : es  un  comando  de símbolo del sistema utilizado para  mostrar una lista de los archivos y subcarpetas contenidos en una carpeta.
- **git checkout**:  se utiliza principalmente para cambiarte de una rama a otra del repositorio.
- **git branch**: este comando administra las ramas creadas en el repositorio. 
- **git commit**: este comando establece un punto de control de tus cambios y los almacena de forma local.
- **git add**: este permite incluir los cambios en los archivos modificados en tu siguiente commit.
- **git push origin**: te permite subir los commits desde tu rama (branch) local en tu repositorio git local al repositorio remoto.
- **git status**: este comando brinda información necesaria sobre la rama actual en la que se está trabajando.
----
- Pull Request del repositorio
A la hora de tener las versiones finales de cada código, lo que se hace en GitHub es hacer un pull request de cada rama externas a la main, este pull request sube los cambios a la main, concatenando las ramas en main.
![](https://i.imgur.com/Y6rnJAX.jpg)
![](https://i.imgur.com/KxtyNhz.jpg)

### Integrantes y sus usuarios de GitHub
**integrantes** | **GitHub User**|
| - | - 
Martin Vallejo | MVB1512
Sofia Urrego | sofiaurego
Ana Paredes | anadan10102006
Marcela Peña| viesyeo

-creado por: Marcela Peña Escobar
-Fecha de creación: 14 de Noviembre de 2023

