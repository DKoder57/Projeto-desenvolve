# Use a biblioteca 'pynput' para criar a movimentação do jogador.
# Use funções 'iniciar_jogador()', 'mover_jogador()' e 'pontuacao_jogador()'.
# *DESAFIO* crie uma função recursiva que retorna os comandos para resolver o labirinto e um botão para assistir a resolução.

from pynput import keyboard
import tkinter as tk

# Variável para armazenar os comandos realizados
script_da_jogada = []
controller = keyboard.Controller()

def iniciar_jogador():
    print("Jogador entrou no labirinto.")
    script_da_jogada.clear()

def mover_jogador(direcao):
    case = {
        'cima': keyboard.Key.up,
        'baixo': keyboard.Key.down,
        'esquerda': keyboard.Key.left,
        'direita': keyboard.Key.right
    }
    if direcao in case:
        tecla = case[direcao]
        controller.press(tecla)
        controller.release(tecla)
        script_da_jogada.append(f"Jogador moveu para {direcao}.")
        print(f"Jogador moveu para {direcao}.")

def pontuacao_jogador():
    pontos = len(script_da_jogada)
    print(f"Pontuação do jogador: {pontos}")
    return pontos

def resolver_labirinto(labirinto, posicao, destino, caminho=None):
    if caminho is None:
        caminho = []
    if posicao == destino:
        return caminho

    x, y = posicao
    movimentos = {
        "cima": (x, y-1),
        "baixo": (x, y+1),
        "esquerda": (x-1, y),
        "direita": (x+1, y)
    }

    for direcao, nova_pos in movimentos.items():
        if nova_pos not in caminho and nova_pos in labirinto:
            resultado = resolver_labirinto(labirinto, nova_pos, destino, caminho + [nova_pos])
            if resultado:
                return [direcao] + resultado
    return None

def assistir_resolucao():
    comandos = resolver_labirinto(
        labirinto={(0,0),(1,0),(1,1),(2,1)},  
        posicao=(0,0),
        destino=(2,1)
    )
    if comandos:
        print("Resolução encontrada:", comandos)
        for cmd in comandos:
            mover_jogador(cmd)
    else:
        print("Não há solução para o labirinto.")

# Interface Tkinter
janela = tk.Tk()
janela.title("Labirinto")

tk.Button(janela, text="Assistir Resolução", command=assistir_resolucao).pack()
tk.Button(janela, text="Mostrar Pontuação", command=pontuacao_jogador).pack()

janela.mainloop()
