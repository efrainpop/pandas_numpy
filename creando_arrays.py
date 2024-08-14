import numpy as np

#lista= list(range(0,10)) #star 0, 10 stop no se incluye 
lista = np.arange(0,10)
lista =np.arange(0,20)
lista =np.arange(0,20,2)#step de dos en dos
lista= np.zeros(3) #array de 3 ceros
lista =np.zeros((10,10)) #crea un array de 10x10 de ceros
lista= np.ones ((10,5))#crea array de 10x5 de unos
lista= np.linspace(0,10,10)
lista= np.linspace(0,10,100)
lista= np.eye(4)
lista= np.random.rand()#manda numero aleatorio
lista=np.random.rand(4)#manda 4 numeros aleatorios
lista=np.random.randn(4,5 )#manda 4 numeros aleatorios
lista=np.random.randint(1,15)#manda un numero aleatorio entre el 1 y el 15
lista=np.random.randint(1,100,(10,10))
print(list)