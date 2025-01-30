import random

counter = 0
pc_counter = 0

for i in range(10):
    user_input = input("Kámen, nůžky nebo papír?")
    computer_choice = random.choice(["kámen", "nůžky", "papír"])

    if computer_choice == user_input:
        print("Remíza")
        print(f"Tvoje skóre: {counter} PC skóre: {pc_counter}")

    elif computer_choice == "kámen" and user_input == "papír":
        print("Výhra")
        counter += 1
        print(f"Tvoje skóre: {counter} PC skóre:  {pc_counter}")
        
    elif computer_choice == "papír" and user_input == "nůžky":
        print("Výhra")
        counter += 1
        print(f"Tvoje skóre: {counter} PC skóre: {pc_counter}")

    elif computer_choice == "nůžky" and user_input == "kámen":
        print("Výhra")
        counter += 1
        print(f"Tvoje skóre: {counter}  PC skóre: {pc_counter}")

    else:
        print("Prohra")
        pc_counter += 1
        print(f"Tvoje skóre: {counter} PC score: {pc_counter}")

if counter >= pc_counter:
    print("Vyhráli jste")
elif pc_counter >= counter:
    print("Počítač vyhrál")
elif pc_counter == counter:
    print("Hra skončila remízou")
