def main():
    print("This program find username")
    print()
    first = input("Enter your firstname : ")
    last = input("Enter your lastname : ")

    uname = first[:4] + last[:4]
    print("Your Username is : ",uname)
main()
