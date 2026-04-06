import sys

input_data = sys.stdin.read().strip()

def last_index(input_data):
    lines = input_data.split("\n")
    n = int(lines[0])
    arr = lines[1].split()
    element = int(lines[2])

    for i in range(n-1, -1, -1):
        if int(arr[i]) == element:
            return i
        
    return -1

index = last_index(input_data)
print("The last occurence of element is: ",index)