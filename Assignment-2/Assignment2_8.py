def main():
    print("Enter your number")
    num = int(input())

    for i in range(num+1):        
        for j in range(1, i+1):  

            print(j, end="")     
        print()   
    
if __name__ == "__main__":
    main()

#chat gpt