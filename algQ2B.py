#algoritimo para o usuario acertar a matriz transposta de 1 2 3 4 5 6 7 8 9 
import numpy as np 
def matriztransposta():
    A = np.array([[1, 2, 3],[4, 5, 6], [7, 8, 9]])
    A = np.transpose(A) 
    print(A)



print('''Acerte o calculo da matriz transposta de:
[1, 2, 3]
[4, 5, 6], 
[7, 8, 9] digite linha por linha e sem espaços''')

usuario = int(int(input("Sua resposta: ")))
if usuario == 147258369:
   print('parabens voce acertou')
   matriztransposta() 
else:
    print("voce errou tente novamente")   

