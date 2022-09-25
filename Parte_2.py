import random as rd
arreglo_1 = [0] * 10
cont = 0
acum = 0
esprimo = True
#ARREGLO CON VALORES RANDOM
for i in range(len(arreglo_1)):
    arreglo_1[i]=rd.randrange(1000)
    cont = cont + 1
    print(f"{cont} {arreglo_1[i]}")
#CONTADOR DE NUMEROS PARES
for i in range(len(arreglo_1)):
    if arreglo_1[i]%2 == 0:
        acum = acum + 1
print(f"La cantidad de elementos pares es : {acum}")
suma = 0
for i in range(len(arreglo_1)):
    if arreglo_1[i]%2!= 0:
        suma = suma + arreglo_1[i]
print(f"La suma de numeros impares es : {suma}")
#ELEMENTOS PRIMOS
'''for i in range(len(arreglo_1)):
    if arreglo_1% ==0:
        print(f"El numero {arreglo_1} es primo")'''
