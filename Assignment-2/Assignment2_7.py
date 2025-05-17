def main():
    print("Enter your number")
    num = int(input())

    for i in range(num):        
        for j in range(1, num + 1):   
            print(j, end="")     
        print()   
    
if __name__ == "__main__":
    main()

#chat gpt