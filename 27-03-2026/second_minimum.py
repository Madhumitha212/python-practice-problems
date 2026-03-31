arr = list(map(int, input("Enter array elements: ").split()))

first_min = second_min = float('inf')

for num in arr:
    if num < first_min:
        second_min = first_min
        first_min = num
    elif first_min < num < second_min:
        second_min = num

# Check if second minimum exists
if second_min != float('inf'):
    print("Second minimum element:", second_min)
else:
    print("No second minimum element exists")