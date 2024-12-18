#house #match
name = input("What's your name? ")
match name:
    case "Harry":
        print("Griffindor")
    case "Hermoine":
        print("Griffindor")
    case "Ron":
        print("Griffindor")
    case"Draco":
        print("Slytherin")
    case _:
        print("Who?")