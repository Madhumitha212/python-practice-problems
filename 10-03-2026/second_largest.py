arr = list(map(int, input("Enter array elements: ").split()))

first_large = second_large = float('-inf')

for num in arr:
    if num > first_large:
        second_large = first_large
        first_large = num
    elif num > second_large and num != first_large:
        second_large = num

print("Second largest element:", second_large)