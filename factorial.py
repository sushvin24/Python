def main():
    print("This program find factorial of number")
    n=int(input("Enter the number to find factorial : "))
    print()
    fact = 1
    for factor in range(n,1,-1):
        fact = fact * factor
    print("The factorial of ",n,"is",fact)
main()
