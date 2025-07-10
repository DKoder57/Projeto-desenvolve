# Atividade 1 - Escreva um script python que use compreensão de listas para criar as seguintes listas:

print("Atividade 1 \n")
import random
    # Todos os números pares entre 20 e 50
A1_Lista_1 = [i for i in range(20, 51) if i % 2 == 0]
print("- Lista de números pares entre 20 e 50:", A1_Lista_1, "\n")

    # Os quadrados de todos os valores da lista
A1_Lista_2 = [ 1,2,3,4,5,6,7,8,9]
A1_Lista_2 = [i**2 for i in A1_Lista_2]
print("- Lista dos quadrados dos valores:", A1_Lista_2, "\n")
    
    # Todos os números entre 1 e 100 que sejam divisíveis por 7
A1_Lista_3 = [i for i in range(1, 100) if i % 7 == 0]
print("- Lista de números divisíveis por 7 entre 1 e 100:", A1_Lista_3 , "\n")
    
    # Para todos os valores em range(0,30,3), escreva "par" ou "ímpar" dependendo da paridade do elemento.
A1_Lista_4 = ["par" if i % 2 == 0 else "ímpar" for i in range(0, 30, 3)]
A1_lista_4s = [i for i in range(0, 30, 3)]

print("- Lista de números de 0 a 30 com passo 3:", A1_Lista_4), print("lista com números:", A1_lista_4s)

# Atividade 2 -  Solicite uma frase do usuário e usando compreensão de listas imprima:
# A lista de vogais da frase, ordenada alfabeticamente
# A lista de consoantes da frase (remova espaços em branco)

print("\n Atividade 2 \n")

Frase = input("Digite uma frase: ")
print("Frase digitada:", Frase)
Vogais = [i for i in Frase if i.lower() in 'aeiou']
Consoantes = [i for i in Frase if i.lower() not in 'aeiou' and i != '']
print("Lista de vogais:", Vogais)
print("Lista de consoantes:", Consoantes)



# Atividade 3 - Reescreva o código a seguir para construir a lista pagamentos usando compreensão de listas, ou seja, eliminando o laço de repetição.

print("\n Atividade 3 \n")

horas_trabalhadas = [40,37,45,40,40,48]
ganho_por_hora = 20
hora_extra = 25
pagamento = []
n_pagamento = 0
for hora in horas_trabalhadas:
    pagamento.clear()
    pagamento.append(ganho_por_hora * min(hora, 40) + hora_extra * max(0, hora - 40))
    n_pagamento += 1
    print(f"Pagamento: ", pagamento, n_pagamento)
    


# Atividade 4 - Reescreva o código a seguir para construir a lista aprovados usando compreensão de listas, ou seja, eliminando o laço de repetição.

print("\n Atividade 4 \n")

alunos = ["João", "José", "Carla", "Sol"]
notas = [35, 50, 20, 80 ]
aprovados = []
for i in range(len(notas)):
    if notas[i] >= 60:
        aprovados.append(alunos[i])
        print(f"Aluno: {alunos[i]} - Nota: {notas[i]} - Aprovado")
    else:
        print(f"Aluno: {alunos[i]} - Nota: {notas[i]} - Reprovado")