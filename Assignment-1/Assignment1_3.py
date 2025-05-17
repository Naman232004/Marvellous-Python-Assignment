def Add(val1 , val2):
    ans = 0 
    ans = val1 + val2
    return ans 

def main():
    print("Enter your first number: ")
    num1 = int(input())
    print("Enter your second number: ")
    num2 = int(input())
    ans = Add(num1 , num2)
    print("Addition is " , ans)

if __name__ == "__main__":
    main()