import random

def escolher_palavra():
    palavras = [
        'desenvolvimento', 'tecnologia', 'logica', 
        'programacao', 'tendencias', 'html', 
        'python', 'maquina', 'terminal', 'dados'
    ]
    return random.choice(palavras)

def exibir_forca(tentativas):
    estagios = [
        '''
           -----
           |   |
               |
               |
               |
               |
        --------
        ''',
        '''
           -----
           |   |
           O   |
               |
               |
               |
        --------
        ''',
        '''
           -----
           |   |
           O   |
           |   |
               |
               |
        --------
        ''',
        '''
           -----
           |   |
           O   |
          /|   |
               |
               |
        --------
        ''',
        '''
           -----
           |   |
           O   |
          /|\  |
               |
               |
        --------
        ''',
        '''
           -----
           |   |
           O   |
          /|\  |
          /    |
               |
        --------
        ''',
        '''
           -----
           |   |
           O   |
          /|\  |
          / \  |
               |
        --------
        '''
    ]
    print(estagios[tentativas])

def jogar():
    palavra = escolher_palavra()
    palavra_oculta = ['_' for _ in palavra]
    tentativas = 0
    letras_tentadas = set()
    
    print("Bem-vindo ao Jogo da Forca!")
    exibir_forca(tentativas)
    print("Palavra: " + " ".join(palavra_oculta))
    
    while True:
        letra = input("Digite uma letra: ").lower()
        
        if letra in letras_tentadas:
            print("Você já tentou essa letra. Tente novamente.")
            continue
        
        letras_tentadas.add(letra)
        
        if letra in palavra:
            for i, char in enumerate(palavra):
                if char == letra:
                    palavra_oculta[i] = letra
        else:
            tentativas += 1
        
        exibir_forca(tentativas)
        print("Palavra: " + " ".join(palavra_oculta))
        
        if "_" not in palavra_oculta:
            print("Parabéns! Você adivinhou a palavra.")
            break
        
        if tentativas == 6:
            print(f"Você perdeu! A palavra era '{palavra}'.")
            break

    print("Obrigado por jogar!")

# Executar o jogo
if __name__ == "__main__":
    jogar()
