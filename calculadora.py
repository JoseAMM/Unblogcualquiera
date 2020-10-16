print("¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬")
print("Calculadora super perronsisima")
print("¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬¬")
#####################################
suma= 1
resta= 2
multiplicacion= 3
division= 4
divisionentera=5
exponente= 6
modulo= 7
#####################################
print("Suma: 1 \n")
print("Resta: 2 \n")
print("Multiplicación: 3 \n")
print("Division: 4")
print("Division Entera: 5 \n")
print("Exponente: 6 \n")
print("Modulo: 7 \n")
####################################
opcion= int(input("Introduce la opcion deseada: \n"))
if opcion== 1:
    print("Haz elegido suma. \n")
    valor1 = float(input("Elige el primer valor: "))
    valor1 += float(input("Elige el segundo valor: "))
    print("El resultado es ", valor1, ".")
elif opcion== 2:
    print("Haz elegido resta. \n")
    valor1 = float(input("Elige el primer valor: "))
    valor1 -= float(input("Elige el segundo valor: "))
    print("El resultado es ", valor1, ".")
elif opcion== 3:
    print("Haz elegido multiplicación. \n")
    valor1 = float(input("Elige el primer valor: "))
    valor1 *= float(input("Elige el segundo valor: "))
    print("El resultado es ", valor1, ".") 
elif opcion== 4:
    print("Haz elegido division. \n")
    valor1 = float(input("Elige el primer valor: "))
    valor1 /= float(input("Elige el segundo valor: "))
    print("El resultado es ", valor1, ".")
elif opcion== 5:
    print("Haz elegido division entera. \n")
    valor1 = float(input("Elige el primer valor: "))
    valor1 //= float(input("Elige el segundo valor: "))
    print("El resultado es ", valor1, ".")
elif opcion== 6:
    print("Haz elegido exponente. \n")
    valor1 = float(input("Elige el primer valor: "))
    valor1 **= float(input("Elige el segundo valor: "))
    print("El resultado es ", valor1, ".")
elif opcion== 7:
    print("Haz elegido modulo. \n")
    valor1 = float(input("Elige el primer valor: "))
    valor1 %= float(input("Elige el segundo valor: "))
    print("El resultado es ", valor1, ".")
