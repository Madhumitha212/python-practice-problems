# Binary Search Function
def binary_search(arr, x):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1

    return -1


# Taking input from user
arr = list(map(int, input("Enter sorted array elements: ").split()))
x = int(input("Enter element to search: "))

result = binary_search(arr, x)

if result != -1:
    print("Element found at index", result)
else:
    print("Element not found")