#print the array elements from starting to middle

import sys

input_data = sys.stdin.read().strip()

def solve(input_data):
    lines = input_data.split("\n")
    n = int(lines[0])
    arr = lines[1].split(" ")
    print(arr)
    
    for i in range(n//2):
        print(arr[i], end=" ")

solve(input_data)