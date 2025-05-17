def check_prime(num):
        if num <= 1:
            return False
        
        n = 2
        while(n<num):
            if(num % n == 0):
                return False
            n = n + 1
        return True
