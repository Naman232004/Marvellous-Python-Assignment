def get_sum(data):
    sum = 0 
    for val in data:
        sum = sum + val
    return sum
    

def main():
    print("Enter number you want to add")
    num  = int(input())

    print("Enter elements")
    data = list()
    for i in range(num):
        n = int(input())
        data.append(n)
    
    print("Entered elements are :")
    for val in data:
        print(val , end=" ")
    print()


    ret = get_sum(data)
    print("sum " ,ret)


if __name__ == "__main__":
    main()