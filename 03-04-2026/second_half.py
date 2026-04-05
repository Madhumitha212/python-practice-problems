arr = list(map(int, input("Enter data:").split()))

def mid_half(arr):
    for i in range(len(arr)//2, len(arr)):
        print(arr[i], end=" ")

mid_half(arr)