import numpy as np
#generamos numero aleartorios entre 1 y 10 con una estructura de 3x2
arr = np.random.randint(1,10,(3,2))
#imprimir la forma original del arreglo
print("forma original: ", arr.shape)
print(arr)
#cambiamos la forma de arreglo de una forma de (1,6)
arr_reshaped = arr.reshape(1,6)
#imprimimos el arreglo del cambio de forma
print("arreglo despues de reshape: ", arr_reshaped)
