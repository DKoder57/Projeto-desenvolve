# Atividade 1 _ Crie uma condição que seja verdadeira ou falso, com base na idade de Cris e Juliana, e imprima se as duas são maiores de idade ou não.
# Arividade 2 _ Ajuste para caso 1 seja adulta como TRUE.

Cris = int(input("Digite a idade de Cris: "))
Juliana = int(input("Digite a idade de Juliana: "))
condicao_idade1 = Cris > 17 , Juliana > 17
condicao_idade2 = Cris > 17 and Juliana > 17
condição_idade3 = Cris > 17 or Juliana > 17
print(f"idade individual {condicao_idade1}\n idade das duas ({condicao_idade2})")
print(f"idade caso uma seja adulta ({condição_idade3})")

# Atividade 3 _ Crie uma condição que verifique um jogador de xadrez, sua idade, se já jogou 3 partidas, quantas venceu e se é considerado bom.

Jogador_n = int(input("Digite a sua idade: "))
Partidas_n = int(input("Digite o número de partidas jogadas: "))
Vitorias_n = int(input("Digite o número de vitórias: "))
condicao_jogador = Jogador_n >= 16 and Jogador_n <= 18 and Partidas_n >= 3 and Vitorias_n >= 2
print(f"Jogador de xadrez com {Jogador_n} anos, jogou {Partidas_n} partidas e venceu {Vitorias_n} vezes. \n Seu status de entrada é: {condicao_jogador}")

#Atividade 4 _ Crie uma condicional para ajudar um mestre a criar seus personagens em uma campanha de RPG. Os pontos de status devem bater com o exigido pela classe.

Classe_RPG = input("Digite a classe do personagem (Guerreiro, Mago, Arqueiro): ").lower()
força = int(input("Digite a força do personagem: "))
magia = int(input("Digite a magia do personagem: "))
Mago = força <= 10 and magia >= 15
Guerreiro = força >= 15 and magia <= 10
Arqueiro = (força and magia > 5) and ( magia and força <= 15)
print(f"O status do personagem é: {Classe_RPG} ; Força: {força} ; Magia: {magia} ")
print(f"Seu status está feito de forma correta? {Mago or Guerreiro or Arqueiro}")

#Atividade 5 _ Crie uma condicional para aposentadoria, pergunte sexo e idade, e verifique se a pessoa pode se aposentar.
sexo = input("Digite seu sexo (Homem/Mulher):")
Idade_n = int(input("Digite sua idade: "))
pode_aposentar = (sexo == "Homem" and Idade_n >= 65) or (sexo == "Mulher" and Idade_n >= 60)
print(f"Sexo: {sexo}, aposentadoria: {pode_aposentar}")

