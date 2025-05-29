# 3.Write a program which contains filter(), map() and reduce() in it. Python application which
# contains one list of numbers. List contains the numbers which are accepted from user. Filter
# should filter out all such numbers which greater than or equal to 70 and less than or equal to
# 90. Map function will increase each number by 10. Reduce will return product of all that
# numbers.
# Input List = [4, 34, 36, 76, 68, 24, 89, 23, 86, 90, 45, 70]
# List after filter = [76, 89, 86, 90, 70]
# List after map = [86, 99, 96, 100, 80]
# Output of reduce = 6538752000


from functools import reduce


Range = lambda No: (No>= 70 and No <=90)
Increase = lambda No: No + 10
Product = lambda No1,No2 : No1*No2

def main():
    Data = []
    print("Enter size : ",end = "")
    size = int(input())

    print("Enter numbers")
    for i in range(size):
        element = int(input())
        Data.append(element)

    FData = list(filter(Range,Data))
    print("Filtered Data : ",FData)

    MData = list(map(Increase,FData))
    print("Mapped Data : ",MData)

    RData = reduce(Product,MData)
    print("The final result is : ",RData)
   


if __name__ == "__main__":
    main()