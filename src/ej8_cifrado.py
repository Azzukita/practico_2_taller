def cifrado_cesar (mensaje, desplazamiento):
        resultado = ""
        for char in mensaje:
            if char.isalpha():
                #determinar el punto de inicio (A o a
                base = ord('A') if char.isupper() else ord ('a')
                #aplicar el desplazamiento y mantener dentro del alfabeto
                nueva_letra = chr((ord(char) - base + desplazamiento) % 26 + base)
                resultado += nueva_letra
            else:
                resultado += char
        return resultado
def descifrar_cesar (mensaje_cifrado, desplazamiento):
    #descifrar es cifrar pero al revés
    return cifrado_cesar (mensaje_cifrado, -desplazamiento)



mensaje = input("Ingrese un mensaje: ")
desplazamiento = int(input("Ingrese el desplazamiento: "))

cifrado = cifrado_cesar(mensaje, desplazamiento)
descifrado = descifrar_cesar(cifrado, desplazamiento)

print(f"Mensaje cifrado:    {cifrado}")
print(f"Mensaje descifrado: {descifrado}")