palavra = "tomate"
chances = 5
achados = "_" * len(palavra) 

while chances > 0:
    print(f"{achados}  Vidas: {chances}")
    letra = input()
    contem = letra in palavra
    if contem:
        posicoes = [i for i, x in enumerate(palavra) if x == letra]
        for i in posicoes:
            achados = list(achados)
            achados[i] = letra
            achados = ''.join(achados)
    else:
        chances -= 1

    
