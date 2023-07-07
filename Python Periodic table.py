import periodictable

def Periodic_table():
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    while True:
        if username == "yea" and password == "ok":
            print()
            print("      Login successful!   ")
            print("--Wellcome to Periodictable!--")
            print()
            
            Atomic_Number = int(input("Enter your Atomic Number: "))
            element = periodictable.elements[Atomic_Number]
            
            print("--------------------------------")
            print("|  Atomic Symbol  :", element.symbol)
            print("|  Atomic Name    :", element.name,)
            print("|  Atomic mass    :", element.mass,)
            print("|  Atomic Density :", element.density,)
            print("--------------------------------")
            
            next_calculation = input("You want to see more Atomic information? yes/no: ")
            if next_calculation == "no":
                break
            else:
                print("Invalid ID...")

Periodic_table()
