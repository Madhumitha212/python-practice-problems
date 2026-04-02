#program to find sum of even numbers in a list

numbers = [1, 2, 3, 4, 5, 6]
even_sum = sum(num for num in numbers if num % 2 == 0)
print("Sum of even numbers:", even_sum)