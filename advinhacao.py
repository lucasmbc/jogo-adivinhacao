numero_secreto = 7

tentativas_max = 3

tentativas = 0

while tentativas < tentativas_max:
    
    palpite = int(input("Tente adivinhar o número (entre 1 e 10): "))
    
    tentativas += 1
    
    if palpite == numero_secreto:
        print("Parabéns! Você acertou!")
        break    

else:
    print(f"Que pena! Você esgotou suas tentativas. O número era, {numero_secreto}.")
