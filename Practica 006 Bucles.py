# while True:  #este es un bucle infinito
 #   print('solo soy un changuito atrapado en este bucle')


Nlargo= -10 #guardamos el numero largo

numero = int(input("mete un numero o teclea -1 para detenerlo\n"))#metemos el primer valor

while numero != -1: #mientras el numero sea diferente a -1
    if numero > Nlargo: #si el numero es mayor al numero largo
        Nlargo = numero #el numero largo sera igual al numero
    numero = int(input("mete un numero o teclea -1 para detenerlo\n")) #pedimos otro numero
print("el numero mas largo es:", Nlargo)#imprimimos el resultado
