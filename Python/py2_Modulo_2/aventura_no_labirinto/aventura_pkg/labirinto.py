# Criar funções criar_labirinto() e imprimir_labirinto().
# Não pode ser uma string ou estrutura pré-escrita no script.
# Adicionar ao menos 2 referências no labirinto para localização do jogador.

def criar_labirinto(largura, altura, paredes, referencias):
    labirinto = [[' ' for _ in range(largura)] for _ in range(altura)]
    
    # Adiciona paredes
    for (x, y) in paredes:
        labirinto[y][x] = '#'
    
    # Adiciona referências (ex: entrada 'E', saída 'S')
    for (x, y, simbolo) in referencias:
        labirinto[y][x] = simbolo
    
    return labirinto


def imprimir_labirinto(labirinto, posicao_jogador):
    # Imprime o labirinto no console com a posição do jogador
    for y, linha in enumerate(labirinto):
        linha_str = ''
        for x, celula in enumerate(linha):
            if (x, y) == posicao_jogador:
                linha_str += 'J'   # Jogador
            else:
                linha_str += celula
        print(linha_str)


# Exemplo de uso
paredes = [(1,1), (2,1), (3,1), (3,2), (3,3)]
referencias = [
    (0,0,'E'),  
    (4,4,'S')   
]

labirinto = criar_labirinto(5, 5, paredes, referencias)
imprimir_labirinto(labirinto, (0,0))
