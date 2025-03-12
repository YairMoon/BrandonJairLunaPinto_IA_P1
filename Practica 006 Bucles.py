# while True:  #este es un bucle infinito
 #   print('solo soy un changuito atrapado en este bucle')


# Nlargo= -10 #guardamos el numero largo

# numero = int(input("mete un numero o teclea -1 para detenerlo\n"))#metemos el primer valor

# while numero != -1: #mientras el numero sea diferente a -1
#     if numero > Nlargo: #si el numero es mayor al numero largo
#         Nlargo = numero #el numero largo sera igual al numero
#     numero = int(input("mete un numero o teclea -1 para detenerlo\n")) #pedimos otro numero
# print("el numero mas largo es:", Nlargo)#imprimimos el resultado

# for i in range(30):#hacemos un bucle de 30
#     print("el valor de i es ahora", i)#imprimimos el valor de i

# for i in range(15,30):#hacemos otro bucle pero esta vez pondremos donde inicia y donde termina
#     print("el valor de i es ahora", i)

#break y continue

# print("\n La instruccion break:")#la instruccion break se utiliza para salir de un bucle
# for i in range(1,6): #hacemos un bucle de 1 a 6
#     if i == 3: #si i es igual a 3
#         break #salimos del bucle
#     print("Dentro del bucle", i)#imprimimos el valor de i
# print("Fuera del bucle")#imprimimos un mensaje

# #continue
# print("\n La instruccion continue:" )#la instruccion continue se utiliza para saltar a la siguiente iteracion
# for i in range(1,6):#hacemos un bucle de 1 a 6
#     if i == 3: #si i es igual a 3
#         continue #saltamos a la siguiente iteracion
#     print("Dentro del bucle", i)#imprimimos el valor de i
#     print("Fuera del bucle")#imprimimos un mensaje

# x = 1 #creamos una variable x y le asignamos 1
# while x < 8 : #mientras x sea menor a 8
#     print(x)    #imprimimos x
#     x += 1 #le sumamos 1 a x
# else: #si no se cumple la condicion
#     print("llegamos al", x) #imprimimos un mensaje