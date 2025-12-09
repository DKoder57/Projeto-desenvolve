# Implemente uma CLI para executar a main.
# Defina 5 elementos. Sugestões: '--name <nome>', '--level <nível>', '--dificult <x>', '--help'.
# Deve conter ao menos 2 opções no menu do jogo.
# Crie uma tabela final para exibir informações do que foi feito pelo jogador ao fim do jogo.
# *DESAFIO* Inclua uma função recursiva no 'utils.py' que cria uma animação de vítoria ou derrota.

import argparse
from aventura_pkg import utils

def menu():
    print("\n=== MENU DO JOGO ===")
    print("1 - Iniciar jogo")
    print("2 - Mostrar pontuação")
    print("3 - Sair")
    escolha = input("Escolha uma opção: ")
    return escolha

def main():
    parser = argparse.ArgumentParser(description="Jogo do Labirinto CLI")
    parser.add_argument("--name", type=str, help="Nome do jogador")
    parser.add_argument("--level", type=int, default=1, help="Nível inicial")
    parser.add_argument("--dificult", type=str, default="normal", help="Dificuldade do jogo")
    parser.add_argument("--helpme", action="store_true", help="Exibe ajuda personalizada")
    parser.add_argument("--debug", action="store_true", help="Modo debug")

    args = parser.parse_args()

    if args.helpme:
        print("Use --name, --level, --dificult para configurar seu jogo.")
        return

    jogador = {
        "Nome": args.name or "Anônimo",
        "Nível": args.level,
        "Dificuldade": args.dificult,
        "Movimentos": 0,
        "Resultado": "Em andamento"
    }

    while True:
        escolha = menu()
        if escolha == "1":
            print(f"\nJogador {jogador['Nome']} iniciou o jogo!")
            jogador["Movimentos"] += 5  # exemplo de jogada
            # Exemplo de lógica simples: se movimentos >= 5, vitória; senão derrota
            if jogador["Movimentos"] >= 5:
                jogador["Resultado"] = "Vitória"
                utils.animacao_vitoria(5)
            else:
                jogador["Resultado"] = "Derrota"
                utils.animacao_derrota(5)
        elif escolha == "2":
            print(f"Pontuação atual: {jogador['Movimentos']} movimentos")
        elif escolha == "3":
            break
        else:
            print("Opção inválida!")

    # Impressão final sem tabulate
    print("\n=== RESULTADO FINAL ===")
    for chave, valor in jogador.items():
        print(f"{chave:12}: {valor}")

if __name__ == "__main__":
    main()
