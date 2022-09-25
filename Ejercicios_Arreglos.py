import random as rd 
print()
print("**** Crear arreglos y asignarles valores aleatorios del 1 al 100 ****\n")
Arreglo=[0]*100
count = 1

for i in range(len(Arreglo)):
    Arreglo[i]=rd.randrange(10)
    print(f"{count}){Arreglo[i]}")
    count=count+1
    if i%2 ==0:
        print (f"{i}) {Arreglo[i]}")





    