def change():
    print("Change Counter")
    print()
    print("Enter the count of each coin type.")
    print()
    quarters = int(input("Quarters : "))
    dimes = int(input("Dimes : "))
    nickels = int(input("Nickels : "))
    pennies = int(input("Pennies : "))
    total = quarters*0.25 + dimes*0.10 + nickels*0.05 + pennies*0.01
    print("The Total Amount of your change is ",total)

change()
