from functools import reduce 
def check(no):
        return 70 <= no <= 90

def incre(no):
        return no+10

def mul(a,b):
        return a*b

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

        Fdata = list(filter(check ,data))
        print("filter output" , Fdata)

        Mdata = list(map(incre,Fdata))
        print("Map output ", Mdata)

        Rdata = reduce(mul,Mdata)
        print("reduce output ", Rdata)

if __name__ == "__main__":
        main()