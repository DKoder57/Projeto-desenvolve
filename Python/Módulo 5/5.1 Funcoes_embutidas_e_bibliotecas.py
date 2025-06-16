# Atividade 1 _ Desenvolva um programa em Python que peça ao usuário para inserir dois números decimais e calcule a diferença absoluta entre esses dois números.

N1 = float(input("Digite o primeiro número: "))
N2 = float(input("Digite o segundo número: "))
diferenca_absoluta = abs(N1 - N2)
print(f"A diferença absoluta entre {N1} e {N2} é: {diferenca_absoluta}")

#Atividade 2 _ Escreva um código que gere n valores inteiros aleatórios entre 0 e 100 e calcule a raíz quadrada da soma dos valores. Peça ao usuário o valor de n.

import random, math
n = int(input("Digite a quantidade de números: "))
soma = 0
for i in range(n):
    soma += random.randint(0, 100)
print(f"A raiz quadrada da soma dos {n} números é: {math.sqrt(soma)}")

# Atividade 3 _ Escreva um programa em Python que utiliza a biblioteca random para gerar um número aleatório entre 1 e 10 e peça ao usuário para adivinhar o número. Forneça feedback se o palpite é muito alto, muito baixo ou correto. Interrompa a execução somente quando o usuário acertar o palpite.

import random
N = random.randint(1,10)
while i != N:
    i = int(input("Adivinhe o número entre 1 e 10: "))
    if i < N:
        print("Muito baixo!")
    elif i > N:
        print("Muito alto!")
    else:
        print(f"Parabéns! Você acertou o número. O número era {N}.")
        
# Atividade 4 _ Escreva um programa em Python que utiliza a biblioteca datetime para exibir a data e hora atuais com a formatação apresentada a seguir:

import datetime
agora = datetime.datetime.now()
data_atual = agora.date()
hora_atual = agora.time()
print(f"Data e hora atuais: {data_atual.strftime('%d/%m/%Y')} e {hora_atual.strftime('%H:%M')}")

# Atividade 5 _ Seu programa deve apresentar para o usuário a lista de emojis disponíveis com o texto correspondente a cada emoji. Em seguida, solicite uma frase codificada ao usuário e apresente ela decodificada com a visualização de emojis (emojizada).

emojis = {
    ":smile:": "😄",
    ":sad:": "😢",
    ":heart:": "❤️",
    ":thumbs_up:": "👍"
}

print("Emojis disponíveis:")
for code, symbol in emojis.items():
    print(f"{code} - {symbol}")

frase = input("Digite uma mensagem com emote: ")

for code, symbol in emojis.items():
    frase = frase.replace(code, symbol)

print("Mensagem emojizada:", frase)
