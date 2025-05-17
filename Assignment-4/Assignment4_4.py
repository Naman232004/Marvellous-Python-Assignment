from functools import reduce 

check = lambda no : (no%2 == 0)

squr = lambda no : no*no

sum_squr = lambda a,b : a+b


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

        Mdata = list(map(squr,Fdata))
        print("Map output ", Mdata)

        Rdata = reduce(sum_squr,Mdata)
        print("reduce output ", Rdata)

if __name__ == "__main__":
        main()