def sum_fact(num):
    factor_sum = 0 
    n  = 1
    while(n < num):
        if(num%n == 0):
            factor_sum += n
        n = n+1
    return factor_sum

def main():
    print("Enter your number")
    num = int(input())

    ret = sum_fact(num)
    print("addition of factors is  " ,ret)

if __name__ == "__main__":
    main()