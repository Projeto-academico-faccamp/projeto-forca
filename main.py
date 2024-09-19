import random
from palavras import lista_palavras


def obter_palavra():
    palavra = random.choice(lista_palavras)
    return palavra.upper()


def jogar(palavra):
    palavra_completa = "_" * len(palavra)   # Cria uma string de "_" do tamanho da palavra
    acertou = False
    letras_tentadas = []
    palavras_tentadas = []
    tentativas = 6
    total_tentativas = 0  # Contador de tentativas
    
    print("Vamos jogar Forca!")
    print(f"A palavra tem {len(palavra)} letras.")  
    print(exibir_forca(tentativas)) 
    print(palavra_completa)
    print("\n")
    
    while not acertou and tentativas > 0: #loop principal
        palpite = input("Por favor, adivinhe uma letra ou palavra: ").upper()
        
        if len(palpite) == 1 and palpite.isalpha():
            total_tentativas += 1  
            
            if palpite in letras_tentadas:
                print("Você já tentou a letra", palpite)
                
            elif palpite not in palavra:
                print(palpite, "não está na palavra.")
                tentativas -= 1
                letras_tentadas.append(palpite) #guarda a tentativa nas letras ja tentadas
                
            else:
                print("Boa,", palpite, "está certa!")
                letras_tentadas.append(palpite)
                palavra_como_lista = list(palavra_completa) #transforma a string "_" em uma lista para modificar
                indices = [i for i, letra in enumerate(palavra) if letra == palpite]
                # Encontra onde a letra aparece na palavra
                
                for indice in indices: # Substitui os "_" pela letra acertada
                    palavra_como_lista[indice] = palpite
                palavra_completa = "".join(palavra_como_lista) # Atualiza a palavra completa 
                
                if "_" not in palavra_completa:
                    acertou = True
                    
        elif len(palpite) == len(palavra) and palpite.isalpha(): #tentativa palavra msm tamanh
            total_tentativas += 1  
            
            if palpite in palavras_tentadas:
                print("Você já tentou a palavra", palpite)
                
            elif palpite != palavra:
                print(palpite, "não é a palavra.")
                tentativas -= 1
                palavras_tentadas.append(palpite) 
                
            else:
                acertou = True
                palavra_completa = palavra
                
        else:
            print("Palpite inválido.")
        print(exibir_forca(tentativas))
        print(palavra_completa)
        print("\n")
        
    if acertou:
        print("Parabéns, você acertou a palavra!")
        print(f"Você venceu em {total_tentativas} tentativas.")
        
    else:
        print("Acabaram as tentativas. A palavra era " + palavra + ". Mais sorte na próxima vez!")


def exibir_forca(tentativas):
    estagios = [
        
        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / \\
           -
        """,

        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |     / 
           -
        """,

        """
           --------
           |      |
           |      O
           |     \\|/
           |      |
           |      
           -
        """,

        """
           --------
           |      |
           |      O
           |     \\|
           |      |
           |     
           -
        """,

        """
           --------
           |      |
           |      O
           |      |
           |      |
           |     
           -
        """,

        """
           --------
           |      |
           |      O
           |    
           |      
           |     
           -
        """,

        """
           --------
           |      |
           |      
           |    
           |      
           |     
           -
        """
    ]
    return estagios[tentativas]


def main():
    palavra = obter_palavra()
    jogar(palavra)
    while input("Jogar novamente? (S/N) ").upper() == "S":
        palavra = obter_palavra()
        jogar(palavra)


if __name__ == "__main__":
    main()
