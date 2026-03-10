elements = list(map(int, input("Enter elements:").split()))

max_element = 0
for i in elements:
    if i > max_element:
        max_element = i

print("Maximum Element: ",max_element)