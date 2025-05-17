def factorial(a):
    fact = 1 
    while(a != 1):
        fact = a*fact
        a = a-1
    return fact

def main():
    print("Enter your number")
    num = int(input())

    if(num == 0 or num == 1):
        print("factorial is" ,1)
        return

    ret = factorial(num)
    print("factorial is" ,ret)




if __name__ == "__main__":
    main()