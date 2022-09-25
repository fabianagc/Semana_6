import random as rd
#ARREGLOS CON VALORES ALEATORIOS
print("\nCrear arreglos y asignarles valores del 0 al 300 : ")
arregloA=[0]*10
arregloB=[0]*10
val_1=1
val_2=1
suma=0
cont=10
var=1
#ARREGLO_1
print("\nArreglo 1 : \n")
for i in range(len(arregloA)):
    arregloA[i]=rd.randrange(300)
    print(f"{val_1}) {arregloA[i]}")
    val_1=val_1+1
print()    
#ARREGLO_2
print("\nArreglo 2 : \n")
for i in range(len(arregloB)):
    arregloB[i]=rd.randrange(300)
    print(f"{val_2}) {arregloB[i]}")
    val_2=val_2+1
#SUMA DE ARREGLOS 1 Y 2
print("\nSuma de arreglos 1 y 2 : \n")
for i in range(len(arregloA)):
    suma=arregloA[i] + arregloB[i]
    print(f"{[i]}{suma}")
    suma=0
#TABLA DE MULTIPLICAR DE LOS ARREGLOS IMPARES DE B
multi=0
for i in range(len(arregloB)):
    if arregloB[i]%2!= 0:
         for x in range (1,10,1):
            
            
            


