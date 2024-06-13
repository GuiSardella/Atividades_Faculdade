import tkinter as tk

class BMICalculator:
    def __init__(self):
        # Inicializa a janela principal
        self.root = tk.Tk()
        
        # Define o título da janela
        self.root.title("Calculadora de IMC")
        
        # Cria e posiciona os rótulos, entradas e botões
        self.create_widgets()
        
        # Inicia o loop principal da interface
        self.root.mainloop()

    def create_widgets(self):
        # Rótulo e entrada para a altura
        self.height_label = tk.Label(self.root, text="Altura (cm):")
        self.height_label.pack()
        
        self.height_entry = tk.Entry(self.root)
        self.height_entry.pack()

        # Rótulo e entrada para o peso
        self.weight_label = tk.Label(self.root, text="Peso (kg):")
        self.weight_label.pack()
        
        self.weight_entry = tk.Entry(self.root)
        self.weight_entry.pack()

        # Botão para calcular o IMC
        self.calculate_button = tk.Button(self.root, text="Calcular IMC", command=self.calculate_bmi)
        self.calculate_button.pack()

        # Rótulo para exibir o resultado do IMC
        self.result_label = tk.Label(self.root, text="")
        self.result_label.pack()

    def calculate_bmi(self):
        try:
            # Obtém os valores de altura e peso das entradas
            height = float(self.height_entry.get()) / 100  # Converte de cm para metros
            weight = float(self.weight_entry.get())
            
            # Calcula o IMC
            bmi = weight / (height ** 2)
            
            # Exibe o resultado no rótulo de resultado
            self.result_label.config(text=f"Seu IMC é: {bmi:.2f}")
            
            # Chama a função para mostrar a categoria do IMC
            self.show_bmi_category(bmi)
        except ValueError:
            # Caso os valores de entrada não sejam válidos, exibe uma mensagem de erro
            self.result_label.config(text="Por favor, insira valores válidos.")

    def show_bmi_category(self, bmi):
        if bmi < 18.5:
            category = "Abaixo do peso"
        elif 18.5 <= bmi < 24.9:
            category = "Peso normal"
        elif 25 <= bmi < 29.9:
            category = "Sobrepeso"
        else:
            category = "Obesidade"
        
        # Atualiza o rótulo de resultado com a categoria do IMC
        self.result_label.config(text=f"Seu IMC é: {bmi:.2f}\nCategoria: {category}")

# Cria uma instância da classe BMICalculator para executar o programa
if __name__ == "__main__":
    app = BMICalculator()
