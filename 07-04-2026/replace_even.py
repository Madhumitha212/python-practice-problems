arr = list(map(int, input("Enter elements: ").split()))

def replace_even(arr):
    for i in range(len(arr)):
        if arr[i]%2==0:
            arr[i] = 0
        
    for i in range(len(arr)):
        print(arr[i], end = " ")

replace_even(arr)

    