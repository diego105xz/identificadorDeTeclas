# Identificador de teclas
import tkinter as tk

def identificar_tecla(event):
    global caixa_texto
    if event.char and event.char.isprintable():
        letter = event.char
        caixa_texto.insert(tk.END, letter)

def main():
    global caixa_texto
    root = tk.Tk()
    root.title("Identificador de Teclas")
    
    caixa_texto = tk.Text(root, bg="white", height=5, width=30)
    caixa_texto.pack(pady=20)

    root.bind("<KeyPress>", identificar_tecla)

    texto = tk.Label(root, text="Pressione uma tecla:")
    texto.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    main()
