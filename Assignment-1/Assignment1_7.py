def div():
    print("Enter Your Number")
    number = int(input())
    if(number >= 0):
        if(number%5 == 0):
            print("Number is divisible by 5")
        else:
            print("Number is not divisible by 5")

if __name__ == "__main__":
    div()