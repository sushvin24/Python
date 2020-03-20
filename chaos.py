def main():
    print("Choas illustration")
    x = float(input("Enter the number between 0 to 1 : "))
    for i in range(10):
        x = 3.9 * x * (1-x)
        print(x)
main()
