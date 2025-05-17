def main():
    print("Enter your number")
    num = int(input())

    for i in range(num):
        count = num -i
        print("*"*count)
    
if __name__ == "__main__":
    main()