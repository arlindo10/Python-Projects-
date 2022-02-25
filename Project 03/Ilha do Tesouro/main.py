# Treasure Island

print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Bem-vindo à Ilha do Tesouro.")
print("Sua missão é encontrar o tesouro.") 

# using these to avoid writing the same "game over" message each time
game_over = False
victory = False

# area 1
print("Você está em uma encruzilhada. Onde você quer ir? Digite \"esquerda\" ou \"direita\".")
# lowercase the choice, just in case
choice1 = input("> ").lower()
if choice1 == "esquerda":

    # area 2
    print("Você veio a um lago. Há uma ilha no meio do lago. Digite \"esperar\" para aguardar um barco. "
          "Digite \"nadar\" para nadar.")
    choice2 = input("> ").lower()
    if choice2 == "nadar":

        # area 3
        print("Você chega à ilha ileso. Há uma casa com 3 portas. "
              "Um \"vermelho\", um \"amarelo\" e um \"azul\". Qual cor você escolhe?")
        choice3 = input("> ").lower()
        if choice3 == "vermelho":
            print("É uma sala cheia de fogo.")
            game_over = True
        elif choice3 == "azul":
            print("Você entrou em uma sala de feras.")
            game_over = True
        elif choice3 == "amarelo":
            print("Você encontrou o tesouro!")
            victory = True
        else:
            print("Você escolheu uma porta que não existe.")
            game_over = True

    else:
        print("Você é atacado por um animal irritado.")
        game_over = True

else:
    print("Você caiu em um buraco.")
    game_over = True

# print the final outcome
if game_over:
    print("Fim do jogo.")
elif victory:
    print("Você ganhou!")