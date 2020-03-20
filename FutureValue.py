def futval():
    print("This program calculates the future value of a 10-year investment.")
    principal = int(input("Enter the principal amount : "))
    apr = int(input("Enter the annualized percentage rate : "))
    for i in range(10):
        principal = principal * (1+apr)
        print("The amount in 10 years : ",principal)

futval()
