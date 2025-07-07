# Atividade 1 - Escreva um script em Python que solicita do usuário uma quantidade indefinida de números inteiros (com pelo menos 4 valores), os armazena em uma lista e, usando fatiamento de listas
print ("Atividade 1\n")

numeros = ""
lista_numeros = []

while numeros != 0:
    numeros = int(input("Digite um número inteiro (0 para sair): "))
    if numeros != 0:
        lista_numeros.append(numeros)
        
print("Lista de números:", lista_numeros)
print("Os 3 primeiros elementos:", lista_numeros[:3])
print("Os 2 últimos elementos:", lista_numeros[:-2])
print("Lista dos índices pares:", lista_numeros[1::2])
print("Lista dos índices ímpares:", lista_numeros[::2],"\n")


# Atividade 2 - Dada uma lista de endereços web (URLs) que sempre começam com "www." e sempre terminam com ".com", use o conceito de fatiamento de listas para criar uma lista dominios com o nome principal de todos os domínios, conforme exemplo a seguir. 
print ("Atividade 2\n")


URLs = ["www.google.com", "www.gmail.com", "www.github.com", "www.yahoo.com", "www.reddit.com"]
dominios = [[corte[4:-4] for corte in URLs]]
print(dominios)
print("Urls originais:", URLs ,"\n")







# Atividade 3 - Crie uma lista com 20 elementos, entre -10 e 10, gerados aleatoriamente. Em seguida encontre o intervalo que possui a maior quantidade de números negativos e delete ele da lista com o operador del. Você deve imprimir a lista antes e depois da deleção.
print ("Atividade 3\n")

import random
lista_elementos = [random.randint(-10, 10) for _ in range (20)]
print("Lista original:", lista_elementos)

negativos = [lista_elementos[i] for i in range(len(lista_elementos)) if lista_elementos[i] < 0]
print("Números negativos:", negativos)
print("Quantidade de números negativos:", len(negativos))

tamanho_intervalo = 5
max_negativos = -1
inicio_maior = 0

for i in range(len(lista_elementos) - tamanho_intervalo + 1):
    fatia = lista_elementos[i:i + tamanho_intervalo]
    negativos = sum(1 for n in fatia if n < 0)
    if negativos > max_negativos:
        max_negativos = negativos
        inicio_maior = i

print(f"Intervalo com mais negativos ({max_negativos}): {lista_elementos[inicio_maior:inicio_maior + tamanho_intervalo]}")
del lista_elementos[inicio_maior:inicio_maior + tamanho_intervalo]
print("Lista após deleção:", lista_elementos)
