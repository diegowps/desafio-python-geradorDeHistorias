"""
gerador_historia_gui.py
-----------------------
Interface gráfica para o Gerador de Histórias usando Tkinter.
Permite ao usuário escolher o tema e gerar histórias por uma janela.
"""
import tkinter as tk
from tkinter import ttk, messagebox
from gerador_historia import gerar_historia, TEMAS

def gerar():
    tema = tema_var.get()
    try:
        historia = gerar_historia(tema)
        resultado_var.set(historia)
    except ValueError as e:
        messagebox.showerror("Erro", str(e))

# Janela principal
root = tk.Tk()
root.title("Gerador de Histórias")
root.geometry("500x300")

# Tema
tema_var = tk.StringVar(value="fantasia")
resultado_var = tk.StringVar()

ttk.Label(root, text="Escolha o tema da história:").pack(pady=10)
temas = list(TEMAS.keys())
tema_menu = ttk.Combobox(root, textvariable=tema_var, values=temas, state="readonly")
tema_menu.pack()

ttkt_btn = ttk.Button(root, text="Gerar História", command=gerar)
ttkt_btn.pack(pady=10)

resultado_label = ttk.Label(root, textvariable=resultado_var, wraplength=480)
resultado_label.pack(pady=20)

root.mainloop()
