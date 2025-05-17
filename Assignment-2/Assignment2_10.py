def cal_sum(num):
    sum = 0
    for i in range(len(num)):
        n = int(num[i])
        sum = sum + n
    return sum


def main():
    print("Enter your number")
    num = str(input())
    
    ret = cal_sum(num)
    print("sum is" , ret)
if __name__ =="__main__":
    main()