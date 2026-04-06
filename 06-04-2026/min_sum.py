import sys

input_data = sys.stdin.read().strip()

def min_sum(input_data):
    lines = input_data.split("\n")
    n = int(lines[0])
    arr = lines[1].split()
    arr = list(map(int, arr))
    arr.sort()

    if n==1:
        return int(arr[0])
    else:
        first_min = int(arr[0])
        sec_min = int(arr[1])
        return first_min + sec_min
    
sum = min_sum(input_data)
print(f"The minimum sum in array is: {sum}")
