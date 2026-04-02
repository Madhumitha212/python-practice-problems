#Count the number of digitis in a positive integer

input_data = input("Enter number ")

def count_digits(input_data):
    num = int(input_data)
    count = 0
    while(num>0):
        count+=1
        num = num//10
    print(f"The number of digits: {count}")

count_digits(input_data)
