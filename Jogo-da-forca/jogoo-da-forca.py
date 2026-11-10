import random

# Lista de palavras do jogo
palavras = ["python", "computador", "programacao", "escola", "teclado"]

# Escolher uma palavra aleatoria
palavra = random.choice(palavras)

# Guardar as letras utilizadas
letras_utilizadas = []

# Numero maximo de tentativas
tentativas = 6

print("===== JOGO DA FORCA =====")
print("Tente descobrir a palavra secreta!")

while tentativas > 0:

    # Mostrar a palavra escondida
    palavra_escondida = ""

    for letra in palavra:
        if letra in letras_utilizadas:
            palavra_escondida += letra + " "
        else:
            palavra_escondida += "_ "

    print("\nPalavra:", palavra_escondida)
    print("Tentativas restantes:", tentativas)
    print("Letras utilizadas:", letras_utilizadas)

    # Verificar se ganhou
    if all(letra in letras_utilizadas for letra in palavra):
        print("\nParabens! Voce ganhou!")
        break

    # Pedir uma letra
    letra = input("Digite uma letra: ").lower().strip()

    # Validar a entrada
    if len(letra) != 1 or not letra.isalpha():
        print("Digite apenas uma letra!")
        continue

    # Verificar letras repetidas
    if letra in letras_utilizadas:
        print("Essa letra ja foi utilizada!")
        continue

    letras_utilizadas.append(letra)

    # Verificar se acertou
    if letra in palavra:
        print("Muito bem! Voce acertou!")
    else:
        print("Voce errou!")
        tentativas -= 1

else:
    print("\nVoce perdeu!")
    print("A palavra era:", palavra)