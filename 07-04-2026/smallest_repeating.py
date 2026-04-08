arr = list(map(int, input("Enter elements: ").split()))

def smallest_repeating(arr):
    li = []
    for i in range(len(arr)-1):
        if arr[i] == arr[i+1]:
            li.append(arr[i])
            arr[i+1] = '$'

    if len(li)!=0:
        li.sort()
        print(li[0])
    else:
        print("-1")

smallest_repeating(arr)
