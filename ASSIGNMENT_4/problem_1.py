# 1.Write a program which contains one lambda function which accepts one parameter and return
# power of two.
# Input : 4 Output : 16
# Input : 6 Output : 64

def main():
    print("Enter a number : ",end = "")
    Value = int(input())
    Square = lambda x: 2**x
    Result = Square(Value)
    
    print(f"The Result is : {Result}")


if __name__ == "__main__":
    main()