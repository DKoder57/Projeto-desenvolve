#Atividade 1 _ Faça um programa que gere aleatoriamente 20 valores inteiros entre -100 e 100 e os armazene em uma lista. Em seguida imprima na ordem estabelecida:
print("Atividade 1\n")
import random

lista_aleatoria = []
for i in range(20):
    valores = random.randint(-100, 100)
    lista_aleatoria.append(valores)
    

print(sorted(lista_aleatoria))  # Imprime a lista ordenada
print(lista_aleatoria)  # Imprime a lista original
print("maior valor:", max(lista_aleatoria))  # Imprime o maior valor
print("menor valor:", min(lista_aleatoria))  # Imprime o menor valor

#Atividade 2 _ Faça um programa que gere aleatoriamente um valor entre 5 e 20 e armazene em uma variável chamada num_elementos. Em seguida gere aleatoriamente valores entre 1 e 10 em quantidade correspondente a num_elementos, e armazene em uma lista chamada elementos. 
print("\nAtividade 2\n")
import random 
num_elements = []
for i in range(5,20):
    valores = random.randint(1, 10)
    num_elements.append(valores)
    
print(num_elements)  # Imprime a lista de elementos gerados
print("Quantidade de elementos:", len(num_elements))  # Imprime a quantidade de elementos
print("Média dos elementos:", sum(num_elements) / len(num_elements))  # Imprime a média dos elementos
    
#Atividade 3 _ Preencha duas listas (lista1, lista2) com 20 valores inteiros aleatórios entre 0 a 50. Crie uma terceira lista interseccao contendo apenas os valores que se repetem nas duas listas. Ao final imprima:
print("\nAtividade 3\n")
import random
listx1 = []
listx2 = []
inersecsione = []
for i in range(20):
    valores1 = random.randint(0, 50)
    valores2 = random.randint(0, 50)
    listx1.append(valores1)
    listx2.append(valores2)

inersecsione = list(set(listx1) & set(listx2))
print("Lista 1:", listx1)  # Imprime a lista 1
print("Lista 2:", listx2)  # Imprime a lista 2
print("Interseção:", inersecsione)  # Imprime a lista de interseção

#Atividade 4 _ Crie um programa em Python que receba duas listas de números do usuário, podendo cada lista ter uma quantidade diferente de valores. Em seguida, combine essas duas listas de forma alternada para formar uma terceira lista. Intercale os elementos até o final da primeira lista, adicionando ao final os elementos remanescentes da maior lista.
print("\nAtividade 4\n")
listosa1 = []
listosa2 = []
intercalada = []
for i in range(5):
    valores1 = int(input("Digite um valor para a lista 1: "))
    listosa1.append(valores1)
    intercalada.append(valores1)  
    valores2 = int(input("Digite um valor para a lista 2: "))
    listosa2.append(valores2)
    intercalada.append(valores2)

print("Lista 1:", listosa1)  # Imprime a lista 1
print("Lista 2:", listosa2)  # Imprime a lista 2
print("Lista Intercalada:", intercalada)  # Imprime a lista intercalada