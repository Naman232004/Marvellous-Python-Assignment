def check_prime(num):
        if num <= 1:
            return False
        
        n = 2
        count = 0
        while(n<num):
            if(num % n == 0):
                count = count + 1
            n = n+1

        if(count == 0):
            return True
        else:
            return False


def main():
        print("Enter number you want to check ")
        num = int(input())
        
        ret = check_prime(num)
        if(ret == True):
            print("It is prime number")
        else:
            print("itis not prime")

if __name__ == "__main__":
        main()