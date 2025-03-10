x = 0  # asignamos 0 a x 
print(x == 0)
                            #operadores comparativos true o false
x = 1  # asigamos 1 a x
print(x == 0)


# comparacion de numeros , cual es mayor
num1 = int(input("ingresa el primer numero : "))
num2 = int(input("ingresa el segundo numero: "))

# elegir el mayor
if num1 > num2: #ponemos una condicion si num1 es mayor que num2
    gran_num = num1
else: # o en dado caso que sea al reves
    gran_num = num2

# mostrar el resultado
print("el numero mas grande es :", gran_num)

##MISMO CODIGO PERO CON MAS NUMEROS Y UTILIZANDO OTRA FUNCION

nume1 = int(input("ingresa el primer numero : ")) #creamos la variable y guardamos 
nume2 = int(input("ingresa el segundo numero "))
nume3 = int(input("ingresa el tercer numero "))

grand_num = max(nume1, nume2, nume3) #max es una funcion que nos ayuda a encontrar el numero mas grande

print("el numero mas grande es :", grand_num)#imprimimos el resultado


