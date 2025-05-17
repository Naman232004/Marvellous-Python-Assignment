from arithmatic import check_prime

def ListPrime(data):
    total = 0
    for val in data:
        if check_prime (val):
            total += val
    return total


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

    ret = ListPrime(data)
    print("sum of prime" , ret)
    

if __name__ == "__main__":
    main()