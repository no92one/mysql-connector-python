import request

def new_user():
    run = True
    while run:
        username = input("Skriv in ett nytt username: ")
        password = input("Skriv in ett nytt lösenord: ")

        answer = input(f"username -> {username}\n"
                       f"lösenord -> {password}\n"
                       "Blir detta bra? (y/n) eller skriv Q för att avsluta: ").strip().lower()
        if answer == "y":
            request.add_user(username, password)
            run = False
        elif answer == "q":
            run = False


run = True
while run:
    answer = input("\nMeny\n"
                   "\n1. Skriv ut alla användare"
                   "\n2. Lägg till en ny användare"
                   "\n3. Ta bort en användare"
                   "\nQ. Avsluta programmet"
                   "\n-> ").strip()

    match answer.lower():
        case "1":
            print("Du valde 1.")
        case "2":
            new_user()
        case "3":
            print("Du valde 3.")
        case "q":
            print("Programmet avslutas!")
            run = False
        case _:
            print(f"'{answer}' är inte ett alternativ, välj mellan 1-3 eller Q!")






