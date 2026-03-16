frase = str(input("Digite a frase:"))
frase = frase.upper().split()
alfabeto = [
    'A','B','C','D','E','F','G','H','I','J','K','L','M',
    'N','O','P','Q','R','S','T','U','V','W','X','Y','Z'
]

for i in range(22):
    resposta = ""
    for j in frase:
        posicaoAlfabeto = alfabeto.index(j)
        posicaoAtualizada = posicaoAlfabeto - i
        resposta += alfabeto[posicaoAtualizada]
      
    print(f"{i} - {resposta}")
    resposta = ""
    
    
