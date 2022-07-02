import numpy as np #importando a biblioteca numpy
def matriztransposta():
    A = np.array([[1, 2, 3],[4, 5, 6], [7, 8, 9]]) #usando a funçao array para transformar uma lista em uma matriz
    A = np.transpose(A) #usando a funçao transpose para fazer o calculo da transposta dessa matriz
    print(A)

matriztransposta() #chamando a funçao
