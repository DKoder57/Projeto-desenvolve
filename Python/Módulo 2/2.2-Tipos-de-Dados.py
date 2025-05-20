##Atividade 1
Valor5_1 = 5
Valor2_1 = 2
resultado5p2 = Valor5_1/Valor2_1
print(resultado5p2)
print(type(resultado5p2))
## Atividade 2

Resultadotxt = "O resultado é "
valor1_2 = 10
valor2_2 = 3.5
soma_2 = valor1_2+valor2_2
print(Resultadotxt, valor1_2, valor2_2, soma_2)
print("Tipos:", type(Resultadotxt), type(valor1_2), type(valor2_2), type(soma_2))

## Atividade 3
v1 = 10
v2 = 20
a1 = v1
v1 = v2
v2 = a1
print('v1 =', v1)
print("v2 =", v2)

## Atividade 4
Valor_salario = 500
rendimento_3_meses = Valor_salario
for _ in range(3):
    rendimento_3_meses *= 1.01
print("Rendimento após 3 meses:", rendimento_3_meses)
