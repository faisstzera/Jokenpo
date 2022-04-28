#Prova
#Alexandre de Freitas Faisst | Eduarda Dallagrana | Nicolas Andreas Jackel |Bruno Teider | Vinicius Teider

import random
gm = 1

#1 = pedra
#2 = papel
#3 = tesoura

while gm != 0:
    # Condição para pedir o input novamente quando o player voltar para o menu
    user = 5 
    pc = 5
    
    print("-"*30)
    print("Jokepô!".center(30))
    print("-"*30)
    print("|1| -> jogar contra a maquina")
    print("|2| -> jogar contra outro player")
    print("|0| -> cancelar")
    
    gm = int(input("Insira como deseja jogar: "))
    if gm == 0:
        break
    while gm != 1 and gm != 2:
        gm = int(input("Número Incorreto. Insira 1 ou 2: "))
    
# Jogo

    print("="*30)
    print("|1| -> Pedra")
    print("|2| -> Papel")
    print("|3| -> Tesoura")
    print("|0| -> Escolher outro modo de jogo")
    print("="*30)

    #Loop para garantir que a partida irá ficar no modo de jogo escolhido  
    while True:

        while user > 3 or user < 0:
            user = int(input("Jogador 1, selecione uma opção de 1 a 3: "))
        if user == 0:   
            break
        
        if gm == 1:
            pc = random.randint(1,3)
            txt = "Máquina"
            vc = "Você"
            
        if gm == 2:
            while pc > 3 or pc < 0:
                pc = int(input("Jogador 2, selecione uma opção de 1 a 3: "))
            if pc == 0:
                break
            txt = "Jogador 2"
            vc = "Jogador 1"
    
    # Comparações e possibilidade de quebra do loop
    
        if user == 1: print(f"{vc} escolheu Pedra.")
        elif user == 2: print(f"{vc} escolheu Papel.")
        elif user == 3: print(f"{vc} escolheu Tesoura.")
        elif user == 0: break
    
        if pc == 1: print(f"{txt} escolheu Pedra.")
        elif pc == 2: print(f"{txt} escolheu Papel.")
        elif pc == 3: print(f"{txt} escolheu Tesoura.")
        elif pc == 0: break
        
        if pc == user:
            print("Vocês jogaram a mesma opção, Empate.")           
        elif (user == 2 and pc == 1) or (user == 1 and pc == 3) or (user == 3 and pc ==2):
            print(f'{vc} ganhou!')
        else:
            print(f'{txt} ganhou!')
        # Condição para pedir o input novamente antes de uma nova rodada
        user = 5
        pc = 5
        
print ('Jogo encerrado!')