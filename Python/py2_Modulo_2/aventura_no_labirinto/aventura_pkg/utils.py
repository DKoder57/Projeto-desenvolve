#Ao menos 2 funções, exemplo: 'imprime_instruções()', 'hub_jogador()'. 
import time

def imprime_instrucoes():
    print("\n=== INSTRUÇÕES DO JOGO ===")
    print("1. Use as setas do teclado para mover o jogador.")
    print("2. O objetivo é chegar até a saída do labirinto.")
    print("3. Evite bater nas paredes (#).")
    print("4. Boa sorte!\n")

def hub_jogador(nome):
    print(f"\n=== HUB DO JOGADOR ===")
    print(f"Bem-vindo, {nome}!")
    print("Escolha uma opção:")
    print("1 - Iniciar jogo")
    print("2 - Ver instruções")
    print("3 - Sair")
    escolha = input("Digite sua escolha: ")
    return escolha

def animacao_vitoria(n, i=0):
    if i >= n:
        print("🎉 Vitória! 🎉")
        return
    print("." * (i+1))
    time.sleep(0.3)
    animacao_vitoria(n, i+1)

def animacao_derrota(n, i=0):
    if i >= n:
        print("💀 Derrota... 💀")
        return
    print("x" * (i+1))
    time.sleep(0.3)
    animacao_derrota(n, i+1)


