pwd = input("Please type the master key: ")

mode = input("What would you like to do today?\n1. Add a new password?\n2. View the existing passwords?\nChoose from: (Add/View)\nPress Q to quit the program.").lower()

while True:
    if mode =="q":
        break

    if mode == "view":
        print("view")
    elif mode == "add":
        print("add")
    else:
        print("Please enter a valid input!")
        continue