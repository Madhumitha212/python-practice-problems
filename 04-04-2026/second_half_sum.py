import sys

data = sys.stdin.read().strip()

def sum(data):
    lines = data.split("\n")
    n = int(lines[0])
    arr = lines[1].split()
    sum = 0
    for i in range(n//2, n):
        sum = sum + int(arr[i])
    print(f"The sum of first half elements are: {sum}")

sum(data)