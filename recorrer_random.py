import random as rd
arreglo =[0] * 100
count = 1
for i in range(len(arreglo)):
    arreglo[i] = rd.randrange(10)
    print(f"{count}){arreglo[i]}")
    count = count + 1
