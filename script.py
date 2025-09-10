"""
script.py
---------
Script padrão para controlar ações do projeto.
Permite rodar o gerador de histórias ou os testes automáticos.
"""
import os
import sys

def menu():
    print("\n--- Menu do Projeto Gerador de Histórias ---")
    print("1. Gerar uma história")
    print("2. Executar testes automáticos")
    print("0. Sair")
    escolha = input("Escolha uma opção: ").strip()
    return escolha

while True:
    op = menu()
    if op == "1":
        os.system(f"python gerador_historia.py")
    elif op == "2":
        os.system(f"python -m unittest test_gerador_historia.py")
    elif op == "0":
        print("Saindo...")
        sys.exit(0)
    else:
        print("Opção inválida. Tente novamente.")
