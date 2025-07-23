# 1 - Escreva um programa que solicita o nome do usuário e o imprime em forma de escada, como indicado no exemplo a seguir.
print("Atividade 1 \n")

nome = input(str("Digite seu nome: "))
for letra in range(len(nome)):
    print(nome[:letra+1])



# 2 - Escreva um programa que solicite ao usuário inserir seu primeiro nome e sobrenome separadamente. Em seguida, concatene essas duas strings e exiba a mensagem de boas-vindas.
print("\n Atividade 2 \n")
Primeiro_nome = input("Digite seu primeiro nome: ")
Sobrenome = input("Digite seu sobrenome: ")
concatenado = (Primeiro_nome + " " + Sobrenome)
print(f"Bem-vindo(a)",concatenado, "!")

# 3 - Escreva um script que dado uma frase conta os espaços em branco.
print("\n Atividade 3 \n")  
Frase_digitada = input("Digite uma frase: ")
espaços_brancos = Frase_digitada.count(" ")
print(f"A frase digitada possui {espaços_brancos} espaços em branco.")

# 4 - Faça um programa que leia um número de celular e, caso o número tenha apenas 8 dígitos, acrescente o 9 na frente. Caso o número já tenha 9 dígitos, verifique se o primeiro dígito é 9. Adicione o separador "-" na sua impressão.
print("\n Atividade 4 \n")
Numero_celular = input("Digite o número do celular (apenas números): ")
no = 0

if len(Numero_celular) == 8:
    Numero_celular = "9" + Numero_celular
elif len(Numero_celular) == 9 and len(Numero_celular[1]) != 9:
    print("Número inválido, o primeiro dígito deve ser 9.")
    no = 1
else:
    print("Número inválido, o número deve ter 8 ou 9 dígitos.") 
    no = 1
if no != 1: 
    print(f"Número de celular: {Numero_celular[:5]}-{Numero_celular[5:]}")


# 5 - Implemente um código que leia uma string do usuário e imprima quantas vogais existem na frase e quais os seus índices da string. Dica: letra in "aeiou". Exemplo:
print("\n Atividade 5 \n")
frase_usuario = input("Digite uma frase: ")
vogais = "aeiou"
indices_vogais = []
for i in range(len(frase_usuario)):
    if frase_usuario[i].lower() in vogais:
        indices_vogais.append(i)
print(f"A frase digitada possui {len(indices_vogais)} vogais.")
print("Os índices das vogais na frase são:", indices_vogais)

# 6 - Dada uma string e uma palavra objetivo, encontre todos os anagramas da palavra objetivo. Anagramas são palavras com os mesmos caracteres rearranjados.
print("\n Atividade 6 \n")
digite_uma_string = input("Digite uma frase com anagramas para a palavra objetivo: ")
palavra_objetivo = input("Digite a palavra objetivo: ")

plavras = digite_uma_string.lower().split(" ")
for anagrama in plavras:
    if sorted(anagrama) == sorted(palavra_objetivo):
        print(f"Anagrama encontrado: {anagrama}")
    else:
        print(f"Não foi encontrado anagrama para a palavra objetivo: {palavra_objetivo}")
    
    

# 7 - Crie a função encrypt() que recebe uma lista de strings e retorna os nomes criptografados, bem como a chave da criptografia. Regras:
    # Chave de criptografia: gere um valor n aleatório entre 1 e 10
    # Substitua cada caracter c pelo caracter c + n. Trabalharemos apenas com o intervalo de caracteres visíveis (entre 33 e 126 na tabela Unicode)
print("\n Atividade 7 \n")

def encrypt(lista_strings):
    import random
    n = random.randint(1, 10)
    encrypted_strings = []
    for string in lista_strings:
        encrypted_string = ''.join(chr((ord(c) - 33 + n) % 94 + 33) for c in string)
        encrypted_strings.append(encrypted_string)
    return encrypted_strings, n

print("Digite uma lista de strings separadas por vírgula:")
entrada = input().split(',')
lista_strings = [s.strip() for s in entrada]
encrypted_strings, chave = encrypt(lista_strings)  
print("Strings criptografadas:", encrypted_strings)
print("Chave de criptografia:", chave)

# 8 - Desenvolva um validador de CPF. Solicite do usuário um CPF na forma XXX.XXX.XXX-XX (lido como string) e imprima "Válido" ou "Inválido". 
    # O primeiro passo é calcular o primeiro dígito verificador. Separamos os primeiros 9 dígitos do CPF (ex: 111.444.777) e multiplicamos cada um dos números, da direita para a esquerda por números crescentes a partir do número 2. Em seguida somamos o resultado e dividimos por 11.
             # Se o resto da divisão for menor que 2, então o dígito é igual a 0 (Zero).
             # Se o resto da divisão for maior ou igual a 2, então o dígito verificador é igual a 11 menos o resto da divisão (11 - resto).
         
    # Para  calcular o segundo dígito vamos usar o primeiro dígito já calculado. Vamos montar a mesma tabela de multiplicação usada no cálculo do primeiro dígito.
             # Se o resto da divisão for menor que 2, então o dígito é igual a 0 (Zero).
             # Se o resto da divisão for maior ou igual a 2, então o dígito verificador é igual a 11 menos o resto da divisão (11 - resto).
print("\n Atividade 8 \n")

CPF_cliente = input("Digite o CPF (formato XXX.XXX.XXX-XX): ")
CPF_cliente = CPF_cliente.replace(".", "").replace("-", "")
if len(CPF_cliente) != 11 or not CPF_cliente.isdigit():
    print("CPF inválido. Certifique-se de que o CPF tem 11 dígitos numéricos.")
else:
    primeiro_digito = sum(int(CPF_cliente[i]) * (10 - i) for i in range(9)) % 11
    if primeiro_digito < 2:
        primeiro_digito = 0
    else:
        primeiro_digito = 11 - primeiro_digito

    segundo_digito = sum(int(CPF_cliente[i]) * (11 - i) for i in range(10)) % 11
    if segundo_digito < 2:
        segundo_digito = 0
    else:
        segundo_digito = 11 - segundo_digito

    if CPF_cliente[-2:] == f"{primeiro_digito}{segundo_digito}":
        print("CPF Válido")
    else:
        print("CPF Inválido") 
        