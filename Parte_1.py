import random as rd
#ARREGLOS CON VALORES ALEATORIOS
print("\nCrear arreglos y asignarles valores del 0 al 500 : ")
arregloA=[0]*100
cont=1
for i in range(len(arregloA)):
    arregloA[i]=rd.randrange(500)
    print(f"{cont}) {arregloA[i]}")
    cont=cont+1
#INDICES PARES
print("\nIndices pares del arreglo : ")
for i in range(len(arregloA)):
    if i%2 == 0:
        print(f"{[i]}){arregloA[i]}")
#VALOR MAXIMO Y POSICION
for i in range(len(arregloA)):
    maximo = 0
    maximo = max(arregloA)
    if maximo == arregloA[i]:
        print(f"\nPosicion del numero maximo : {[i]}")
print(f"\nNumero maximo : {maximo}")
#VALOR MENOR
for i in range(len(arregloA)):
    minimo = 0
    minimo = min(arregloA)
    if minimo == arregloA[i]:
        print(f"\nPosicion del numero minimo : {[i]}")
print(f"\nNumero minimo : {minimo}\n\n")
#COPIA ARREGLO, MULTIPLICACION * 3, SUMA TOTAL, PROMEDIO
arregloB = arregloA.copy()
total = 0
multi = 0 
promedio = 0
for i in range(len(arregloB)):
    multi = arregloB[i] * 3
    total = total + multi
    
    print(f"{[i]} Multimplicacion * 3 : {multi}")
print(f"\n\nLa suma total de los numeros multiplicados es : {total}\n\n")
promedio = total / 100
print(f"\n\nEl promedio de los numeros multiplicados es : {promedio}\n\n")
    


