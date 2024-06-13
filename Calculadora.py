def adicionar(x, y):
    return x + y

def subtrair(x, y):
    return x - y

def multiplicar(x, y):
    return x * y

def dividir(x, y):
    if y == 0:
        return "Erro: Divisão por zero não é permitida."
    return x / y

def main():
    while True:
        # Exibir o menu de opções
        print("Selecione a operação desejada:")
        print("1. Adicionar")
        print("2. Subtrair")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Sair")

        # Capturar a escolha do usuário
        escolha = input("Digite sua escolha (1/2/3/4/5): ")

        # Verificar se o usuário quer sair
        if escolha == '5':
            print("Obrigado por usar a calculadora. Até mais!")
            break

        # Verificar se a escolha é válida
        if escolha in ['1', '2', '3', '4']:
            try:
                # Guarda os números para a operação
                num1 = float(input("Digite o primeiro número: "))
                num2 = float(input("Digite o segundo número: "))

                # Executar a operação correspondente
                if escolha == '1':
                    print(f"Resultado: {num1} + {num2} = {adicionar(num1, num2)}")
                elif escolha == '2':
                    print(f"Resultado: {num1} - {num2} = {subtrair(num1, num2)}")
                elif escolha == '3':
                    print(f"Resultado: {num1} * {num2} = {multiplicar(num1, num2)}")
                elif escolha == '4':
                    resultado = dividir(num1, num2)
                    print(f"Resultado: {num1} / {num2} = {resultado}")

            except ValueError:
                print("Entrada inválida. Por favor, digite números válidos.")
        else:
            print("Escolha inválida. Por favor, selecione uma opção de 1 a 5.")

# Executar o programa principal
if __name__ == "__main__":
    main()
