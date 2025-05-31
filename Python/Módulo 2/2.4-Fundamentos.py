#Atividade 1_ Calculo de terreno em inteiros

Terreno = 250 #m²
Custo_terreno = 512490.00 #R$

Comprimento = int(input("Digite o comprimento do terreno : "))
Largura = int(input("Digite a largura do terreno : "))
preço_m2 = float(input("Digite o preço do m² : "))

area1 = Comprimento * Largura #m²
preço_total = area1 * preço_m2 #R$

print("Área do terreno:", area1, "m²")
print("Preço total do terreno: R$", preço_total)
print ("Ou")
print(f"Área do terreno: {area1} m² com preço total de R$ {preço_total:,.2f}")

#Atividade 2_ Converta o valor inteira de farenheit para celsius

 #resolução deve estar : 86°F = 30°C
Farenheit = int(input("Digite a temperatura em Fahrenheit: "))
Celsius = int((Farenheit - 32) * 5 / 9)
print(f"{Farenheit}ºF é igual a {Celsius}ºC") 

#Atividade 3_ escreva um código que solicite o usuário, preço e quantidade de 3 produtos e imprima o total.

Nome_usuario = input("Digite seu nome: ")
Preço_unidade = int(input("Digite o preço unitário do produto: R$ "))
Quantidade = int(input("Digite a quantidade do produto: "))
Total_preço_produto = float(Preço_unidade * Quantidade)
print(f"{Nome_usuario}, o total a pagar pelo produto é: R$ {Total_preço_produto:,.2f}")


#Atividade 4_ Escreva um programa que leia o valor e dê a menor quantidade que pode ser trocada em cédulas de 100, 50, 20, 10, 5, 2 e 1 reais.

valor_saque = int(input("Digite o valor do saque: R$ "))
cedulas_100 = valor_saque // 100
valor_saque = valor_saque % 100
cedulas_50 = valor_saque // 50
valor_saque = valor_saque % 50
cedulas_20 = valor_saque // 20
valor_saque = valor_saque % 20
cedulas_10 = valor_saque // 10
valor_saque = valor_saque % 10
cedulas_5 = valor_saque // 5
valor_saque = valor_saque % 5
cedulas_2 = valor_saque // 2
valor_saque = valor_saque % 2
print(f"Cédulas de R$ 100: {cedulas_100}")
print(f"Cédulas de R$ 50: {cedulas_50}")    
print(f"Cédulas de R$ 20: {cedulas_20}")
print(f"Cédulas de R$ 10: {cedulas_10}")
print(f"Cédulas de R$ 5: {cedulas_5}")
print(f"Cédulas de R$ 2: {cedulas_2}")