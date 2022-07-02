frases = [] #declarando uma lista vazia para receber os valores 

frases.append(input( "digite uma frase: " )) #entrada da primeira frase e adicionando ela a lista

frases.append(input( "digite outra frase: " )) #entrada da segunda frase e adicionando ela a lista

frases.append(input( "digite a ultima frase: " )) #entrada da terceira frase e adicionando ela a lista
x = len(frases)
frases.sort() #usando a funçao sort para  ordenar os itens de uma lista em ordem alfabetica
for c in range(x):
    print(f'{frases[c]}',end='')


