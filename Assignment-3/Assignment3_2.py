def get_max(data):
    num = 0 
    for val in data:
        if(val > num ):
            num = val
    return num
    
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

    ret = get_max(data)
    print("maximum element is : " ,ret)

if __name__ == "__main__":
    main()