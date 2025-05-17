def main() :
    print("Enter your number")
    number = int(input())
    if(number == 0):
        print("Number is zero")
    elif(number > 0):
        print("Number is Positive")
    elif(number < 0):
        print("Number is Negative")

if __name__ == "__main__":
    main()