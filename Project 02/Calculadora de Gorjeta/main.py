# Tip Calculator

# initialize the variables as empty strings, since input() returns strings
base_bill = ""
percentage = ""
people = ""

print("Bem-vindo à calculadora de gorjetas.")

# get the base bill without tip
while True:
    print("Qual foi o valor total da conta?")
    base_bill = input("> $")
    # check if it can be converted to a float
    try:
        float(base_bill)
        # check if it's not a negative number
        # zero is fine, as they might be eating for free... not much sense asking for the other inputs then though
        if float(base_bill) < 0:
            print("A conta não pode ser negativa. Insira um valor válido.")
        # otherwise it should be fine
        else:
            break
    # if not, ask again
    except ValueError:
        print("Insira um valor válido.")

# get the percentage
while True:
    print("Que porcentagem de gorjeta você gostaria de dar? 10, 12 ou 15?")
    percentage = input("> ")
    # list of acceptable choices
    choices_list = ["10", "12", "15"]
    # make sure the input is one of them
    if percentage not in choices_list:
        print("Digite 10, 12 ou 15.")
    else:
        break

# get the number of people
while True:
    print("Quantas pessoas para dividir a conta?")
    people = input("> ")
    # make sure it's a non-zero natural number
    if not people.isdigit() or people == "0":
        print("Insira um número válido de pessoas (1,2,3, etc.)")
    else:
        break

# add the tip to the base bill
total_bill = float(base_bill) * (1 + int(percentage) / 100)

# calculate the split bill and round to 2 decimal places
# since the number of people can't be zero, no need to worry about division by zero
split_bill = round(total_bill / int(people), 2)

# using a uniform message, even if there was just a single person
print(f"Cada pessoa deve pagar: ${split_bill}")