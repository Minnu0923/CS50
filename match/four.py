#house #match
name = input("What's your name? ")
match name:
    case "Harry" | "Hermoine" | "Ron": # | means union
        print("Griffindor")
    case"Draco":
        print("Slytherin")
    case _:
        print("Who?")