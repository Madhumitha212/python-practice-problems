import sys

input_data = sys.stdin.read().strip()

def even_index(input_data):
    lines = input_data.split("\n")
    n = int(lines[0])
    arr = lines[1].split()

    for i in range(0, n, 2):
        print(arr[i], end=" ")

even_index(input_data)