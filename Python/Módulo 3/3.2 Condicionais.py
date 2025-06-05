# Atividade 1 _ Escreva uma condicional de par ou ímpar.

Digite_num = int(input("Digite um número: "))
if Digite_num % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")
    
# Atividade 2 _ Escreva uma condicional de classificação de filmes, ranqueados de 1 a 5 estrelas.

Classificacao = int(input("Digite a classificação do filme (1 a 5): "))
if Classificacao == 1:
    print("O filme é muito ruim.")
elif Classificacao == 2:
    print("O filme é ruim.")
elif Classificacao == 3:
    print("O filme é regular.")
elif Classificacao == 4:
    print("O filme é bom.")
elif Classificacao == 5:
    print("O filme é excelente.")

#Atividade 3 _ Escreva uma condicional para anos bissextos.

Ano = int(input("Digite um ano: "))
if (Ano % 4 == 0 and Ano % 100 != 0) or (Ano % 400 == 0):
    print(f"{Ano} é um ano bissexto.")
else:
    print(f"{Ano} não é um ano bissexto.")

Ano = 1900
if (Ano % 4 == 0 and Ano % 100 != 0) or (Ano % 400 == 0):
    print(f"{Ano} é um ano bissexto.")
else:
    print(f"{Ano} não é um ano bissexto.")

Ano = 2000
if (Ano % 4 == 0 and Ano % 100 != 0) or (Ano % 400 == 0):
    print(f"{Ano} é um ano bissexto.")
else:
    print(f"{Ano} não é um ano bissexto.")

Ano = 2017
if (Ano % 4 == 0 and Ano % 100 != 0) or (Ano % 400 == 0):
    print(f"{Ano} é um ano bissexto.")
else:
    print(f"{Ano} não é um ano bissexto.")        

# Atividade 4 _ Escreva que calcule e entregue informação de entrega de acordo com algumas regras.

Distancia = int(input("digite a distância de entrega em Km: "))
Peso = float(input("digite o peso em Kg do produto: "))
Valor_total = 0.00
if Distancia <= 100*1000:
    Valor_kg  = 1.00
elif Distancia > 100*1000 and Distancia <= 300*1000:
    Valor_kg = 1.50
elif Distancia > 300*1000:
    Valor_kg = 2.00
if Peso > 10.00:
    Valor_total += 10.00
print(f"Distância de: {Distancia:.2f} Km, Peso de entrega: {Peso} Kg")
print(f"Valor total da entrega: R$ {Valor_total + (Peso * Valor_kg):.2f}")

