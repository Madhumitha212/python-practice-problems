# Program to find the factors of a number

num = int(input("Enter number: "))
print(f"The factors of {num} are: ")

def factors(num):
    for i in range(1, num+1):
        if i%2==0:
            print(i, end=" ")

factors(num)