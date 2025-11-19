"""
Interface de linha de comando com argparse.
"""

import argparse
from Personalizado import layout, painel, progresso, estilo

modulos = {
    "layout": layout,
    "painel": painel,
    "progresso": progresso,
    "estilo": estilo
}

def main():
    parser = argparse.ArgumentParser(description="Personalizador com Rich")
    parser.add_argument("texto", help="Texto ou arquivo")
    parser.add_argument("-a", "--arquivo", action="store_true", help="Se for arquivo")
    parser.add_argument("-m", "--modulo", choices=modulos.keys(), required=True)
    parser.add_argument("-f", "--funcao", required=True)

    args = parser.parse_args()
    modulo = modulos[args.modulo]
    funcao = getattr(modulo, args.funcao)
    funcao(args.texto, args.arquivo)

if __name__ == "__main__":
    main()
