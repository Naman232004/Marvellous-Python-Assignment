from arithmatic import Add , Sub , Mul ,Div

def main():
    print("Enter first number")
    a = int(input())
    print("Enter second number")
    b = int(input())

    ret = Add(a,b)
    print("Addition is ", ret)
    ret = Sub(a,b)
    print("Subtraction is ", ret)
    ret = Mul(a,b)
    print("Multiplication is ",ret)
    ret = Div(a,b)
    print("Division is",ret)


if __name__ =="__main__":
    main()