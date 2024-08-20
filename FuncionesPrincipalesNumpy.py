import numpy as np
#definamos numero aleatorios de 1 a 20 en un vector
arr = np.random.randint(1,20,10)
print(arr)  
#ahora lo llevaremos a una estructura matricial
matriz = arr.reshape(2,5)
print(matriz)
#con max voy a traer el numero mas grande que tenga nuestro arr
maximo = np.max(arr)
print(maximo)
maximo=matriz.max()
print(maximo)
#creamos un arr de dos dimensiones
a= np.array ([[1,2,],[3,4]])
b= np.array ([[5,6]])
             #que pasa cuando quieres unir el array b con el array  
             # 
c=np.concatenate((a,b),axis=0)
print(c)       