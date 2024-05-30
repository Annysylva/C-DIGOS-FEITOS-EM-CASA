import tkinter as tk
from tkinter import messagebox

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Erro! Divisão por zero."
    else:
        return x / y

def calculate():
    num1 = float(entry1.get())
    num2 = float(entry2.get())
    choice = operation.get()

    if choice == "1":
        result = add(num1, num2)
    elif choice == "2":
        result = subtract(num1, num2)
    elif choice == "3":
        result = multiply(num1, num2)
    elif choice == "4":
        result = divide(num1, num2)
    else:
        result = "Operação inválida"

    messagebox.showinfo("Resultado", f"O resultado é: {result}")

# Configuração da janela principal
root = tk.Tk()
root.title("Calculadora")

# Rótulos e campos de entrada para os números
label1 = tk.Label(root, text="Digite o primeiro número:")
label1.grid(row=0, column=0)
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1)

label2 = tk.Label(root, text="Digite o segundo número:")
label2.grid(row=1, column=0)
entry2 = tk.Entry(root)
entry2.grid(row=1, column=1)

# Rótulo e campo de seleção para a operação
label3 = tk.Label(root, text="Selecione a operação:")
label3.grid(row=2, column=0)
operation = tk.StringVar(value="1")
operations = [
    ("Adição", "1"),
    ("Subtração", "2"),
    ("Multiplicação", "3"),
    ("Divisão", "4")
]
for text, value in operations:
    tk.Radiobutton(root, text=text, variable=operation, value=value).grid(sticky="w")

# Botão para realizar o cálculo
calc_button = tk.Button(root, text="Calcular", command=calculate)
calc_button.grid(row=3, columnspan=2)

# Inicia o loop principal da aplicação
root.mainloop()
