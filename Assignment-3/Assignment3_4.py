def get_freq(data ,a):
    count = 0 
    for val in data:
        if(val == a):
            count = count + 1
    return count

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

    print("Enter element of which you want frequency : ")
    a = int(input())

    ret = get_freq(data ,a)
    print("the number come for ", ret ,"times")



if __name__ == "__main__":
    main()