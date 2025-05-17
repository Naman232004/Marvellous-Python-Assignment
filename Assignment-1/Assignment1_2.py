def ChkNum():
    print("Enter Your Number")
    number = int(input())
    if(number >= 0):
        if(number%2 == 0):
            print("Number is even")
        else:
            print("Number is odd")

if __name__ == "__main__":
    ChkNum()