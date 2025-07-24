# 1 - Faça um programa que solicite a data de nascimento (dd/mm/aaaa) do usuário e imprima a data com o nome do mês por extenso. Dica: usando listas você não precisa fazer um "if" para cada mês.
print("Atividade 1 \n")
data_nascido = input("Digite sua data de nascimento (dd/mm/aaaa): ")
dias, meses, anos = data_nascido.split("/")
meses = int(meses)
meses_extenso = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", 
                "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
print(f"Você nasceu no dia {dias} de {meses_extenso[meses - 1]} de {anos}.")


# 2 - Desenvolva um programa que solicite ao usuário inserir uma frase e substitua todas as ocorrências de vogal por "*".
print("\n Atividade 2 \n")
frase_sub = input("Digite uma frase: ")
vogais = 'aeiouAEIOU'
for vogal in vogais:
     frase_sub = frase_sub.replace(vogal, '*')
print(f"A frase com vogais substituídas é: {frase_sub}")

# 3 - Desenvolva um programa que verifique se uma frase fornecida pelo usuário é um palíndromo (ou seja, lida da mesma forma de trás para frente). Ignore espaços em branco ou sinais de pontuação, e considere maiúsculas e minúsculas da mesma forma. Seu programa deve continuar rodando até que o usuário digite "Fim".
print("\n Atividade 3 \n")
frase_palíndromo = ' '
while frase_palíndromo.lower() != "fim":
 frase_palíndromo = input("Digite uma frase(verificaremos se é um palídromo['fim' para parar]): ")
 frase_p_limpa = ''.join(caracter.lower() for caracter in frase_palíndromo if caracter.isalnum())
 if frase_p_limpa == frase_p_limpa[::-1]:
     print(f"A frase {frase_palíndromo} é um palíndromo.")
 else:
     print(f"A frase {frase_palíndromo} não é um palíndromo.")
 
# 4 - Implemente uma função em Python chamada validador_senha() que verifica se uma senha fornecida atende todos os seguintes critérios:
     # Pelo menos 8 caracteres de comprimento.
     # Contém pelo menos uma letra maiúscula e uma letra minúscula.
     # Contém pelo menos um número.
     # Contém pelo menos um caractere especial (por exemplo, @, #, $).
print("\n Atividade 4 \n")

def validador_senha(senha):
     if len(senha) < 8:
          return print("A senha deve ter pelo menos 8 caracteres.") 
     if not any(c.isupper() for c in senha):
          return print("A senha deve conter pelo menos uma letra maiúscula.")
     if not any(c.islower() for c in senha):
          return print("A senha deve conter pelo menos uma letra minúscula.")
     if not any(c.isdigit() for c in senha):
          return print("A senha deve conter pelo menos um número.")
     if not any(c in '@#$%&*!' for c in senha):
          return print("A senha deve conter pelo menos um caractere especial (@, #, $, etc.).")
     return True
senha = input("Digite uma senha para validação: ")
if validador_senha(senha):
     print("Senha válida.")
else:
     print("Senha inválida.")

# 5 - Implemente uma função chamada embaralhar_palavras() que recebe uma frase como entrada e retorna uma nova frase com as letras internas de cada palavra embaralhadas. Mantenha sempre o primeiro e último caractere da palavra no lugar. 
     # Dica: use a biblioteca random.
print("\n Atividade 5 \n")
import random
def embaralhar_palavras(frase):
    palavras = frase.split()
    nova_frase = []
    
    for palavra in palavras:
        if len(palavra) > 2:
            meio = list(palavra[1:-1])
            random.shuffle(meio)
            nova_palavra = palavra[0] + ''.join(meio) + palavra[-1]
        else:
            nova_palavra = palavra
        nova_frase.append(nova_palavra)
    return ' '.join(nova_frase)

frase = input("Digite uma frase para embaralhar as palavras: ")
frase_embaralhada = embaralhar_palavras(frase)
print(f"A frase com as palavras embaralhadas é: {frase_embaralhada}")