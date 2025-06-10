# Atividade centrada no laço de repetição pela utilização de "While"
# Atividade 1 - Reproduzir o exemplo de fluxograma na atividade em código.

X = int(input("Digite um número: "))
while X > 5:
    print(f"Valor de X é maior que 5: {X}")
    X -= 1  # exemplo para decrementar X e evitar loop infinito
print("fim")

# Atividade 2 - Reproduzir o exemplo de fluxograma na atividade em código.

N = int(input("Digite um número: "))
cont = 0
while cont < N:
    cont += 1
    print(cont)
print("fim")

# Atividade 3 - Reproduzir o exemplo de fluxograma na atividade em código.

N1,N2,N3 = int(input("Digite o primeiro número: ")), int(input("Digite o segundo número: ")), int(input("Digite o terceiro número: "))
m = (N1 + N2 + N3) / 3 # média entre os três números
while True:
    if m >= 60:
        print(f"{m}, nota aprovada.")
        break
    elif 40 <= m < 60:
        print(f"{m}, nota de recuperação.")
        break
    else:
        print(f"{m}, nota reprovada.")
        break
print("fim")

# Atividade 4 - Reproduzir o exemplo de fluxograma na atividade em código.

N = int(input("Digite um número: "))
maior = 0
while N > 0:
    x = int(input("Digite um número: "))
    if x > maior:
        maior = x
    N -= 1
print(maior)

# Atividade 5 - Um instituto realizou uma pesquisa de público e precisa calcular a média de idade dos respondentes. 

n = int(input("Digite um número: "))
soma = 0
cont = 0
while cont < n:
    idade = int(input("Digite a idade: "))
    soma += idade
    cont += 1
    print(f"Soma das idades: {soma/n}") 
    
# Atividade 6 -  Maria precisa de sua ajuda para organizar os experimentos de seu laboratório. Ela quer saber no final do ano, quantas cobaias foram utilizadas no laboratório e o percentual de cada tipo de cobaia utilizada.
# Este laboratório utiliza três tipos de cobaias: sapos, ratos e coelhos. 

n = int(input("Digite o número TOTAL de cobaias: "))
cont = 0
sapos, ratos, coelhos = 0, 0, 0

while cont < n:
    tipo = input("Digite o tipo de cobaia (sapo, rato, coelho): ")
    quantidade = int(input("Digite a quantidade de cobaias: "))
    
    if tipo == "sapo":
        sapos += quantidade
    elif tipo == "rato":
        ratos += quantidade
    elif tipo == "coelho":
        coelhos += quantidade
    else:
        print(f"Tipo de cobaia {tipo} inválido.")
    cont += 1
print(f"Total de cobaias: {sapos + ratos + coelhos}")
print(f"Total de sapos: {sapos}; Total de coelhos: {coelhos}; Total de ratos: {ratos}. \n Percentual: {sapos / (sapos + ratos + coelhos) * 100:.2f}%")
    