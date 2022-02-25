# Band Name Generator

print("Bem-vindo ao gerador de nomes de bandas")

# initialize the variables as empty strings
name = ""
pet_name = ""

# simple check to make sure the user has entered something
while True:
    print("Qual é o nome mais engraçado que você conhece?")
    name = input("> ")
    # if there's no input, ask again
    if name == "":
        print("Você não digitou nada. Por favor, tente novamente.")
    # if there's any input at all, break out of the loop
    else:
        break

# do the same for the pet name
while True:
    print("Qual é o nome do teu animal de estimação?")
    pet_name = input("> ")
    if pet_name == "":
        print("Você não digitou nada. Por favor, tente novamente.")
    else:
        break

# output using f-strings makes the code much more readable
print(f"O nome da sua banda pode ser {name} {pet_name}.")