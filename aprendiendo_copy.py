import numpy as np
arr = np.arange(0,11)
print(arr)
trozo_de_arr = arr[0:6]
print(trozo_de_arr)
#a toso mi array le quiero quitar todos los valores y dejarlos en cero
trozo_de_arr[:] = 0
print(trozo_de_arr)
print(arr)
# sia hora imprimimos el array completo, veras que todos los valores han sido cambiados
print(arr)
#para solucionar esto, utilizamos el comandop copy
arr_copy = arr.copy()
arr_copy[:] = 100
print(arr_copy)
#no obstante la lista original es respetada
print(arr)