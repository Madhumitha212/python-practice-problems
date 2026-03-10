def linear_search(arr, x):
    for i in range(len(arr)):
        if arr[i] == x:
            return i
    return -1


n = int(input("Enter number of elements: "))
arr = []

for i in range(n):
    num = int(input())
    arr.append(num)

print(arr)
x = int(input("Enter a target value:"))

result = linear_search(arr, x)

if result != -1:
    print("Element found at index", result)
else:
    print("Element not found")