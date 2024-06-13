import tkinter as tk
from tkinter import messagebox

class ToDoListApp:
    def __init__(self):
        # Inicializa a janela principal
        self.root = tk.Tk()
        
        # Define o título da janela
        self.root.title("Lista de Tarefas")
        
        # Lista de tarefas
        self.tasks = []

        # Cria e posiciona os elementos da interface
        self.create_widgets()
        
        # Inicia o loop principal da interface
        self.root.mainloop()

    def create_widgets(self):
        # Rótulo para a tarefa
        self.task_label = tk.Label(self.root, text="Digite a tarefa:")
        self.task_label.pack()
        
        # Entrada para a tarefa
        self.task_entry = tk.Entry(self.root)
        self.task_entry.pack()

        # Botão para adicionar a tarefa
        self.add_task_button = tk.Button(self.root, text="Adicionar Tarefa", command=self.add_task)
        self.add_task_button.pack()

        # Listbox para exibir as tarefas
        self.task_listbox = tk.Listbox(self.root)
        self.task_listbox.pack()

        # Botão para remover a tarefa selecionada
        self.remove_task_button = tk.Button(self.root, text="Remover Tarefa", command=self.remove_task)
        self.remove_task_button.pack()

    def add_task(self):
        # Obtém a tarefa da entrada
        task = self.task_entry.get()
        if task:
            # Adiciona a tarefa à lista
            self.tasks.append(task)
            # Atualiza a exibição da lista
            self.update_tasks_listbox()
            # Limpa a entrada
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Aviso", "Você deve digitar uma tarefa.")

    def remove_task(self):
        try:
            # Obtém a tarefa selecionada
            selected_task_index = self.task_listbox.curselection()[0]
            # Remove a tarefa da lista
            self.tasks.pop(selected_task_index)
            # Atualiza a exibição da lista
            self.update_tasks_listbox()
        except IndexError:
            messagebox.showwarning("Aviso", "Você deve selecionar uma tarefa para remover.")

    def update_tasks_listbox(self):
        # Limpa a listbox
        self.task_listbox.delete(0, tk.END)
        # Adiciona todas as tarefas à listbox
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)

# Cria uma instância da classe ToDoListApp para executar o programa
if __name__ == "__main__":
    app = ToDoListApp()
