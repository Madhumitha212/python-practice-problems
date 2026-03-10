arr = list(map(int, input("Enter array elements: ").split()))

min_value = arr[0]

for i in arr:
    if i < min_value:
        min_value = i

print("Minimum element:", min_value)