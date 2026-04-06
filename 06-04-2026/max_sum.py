import sys

input_data = sys.stdin.read().strip()

def max_sum(input_data):
    lines = input_data.split("\n")
    n = int(lines[0])
    arr = lines[1].split()
    arr = list(map(int, arr))
    arr.sort()
    print(arr)

    if n==1:
        return int(arr[0])
    else:
        first_max = int(arr[n-1])
        sec_max = int(arr[n-2])
        return first_max + sec_max
    
print(max_sum(input_data))