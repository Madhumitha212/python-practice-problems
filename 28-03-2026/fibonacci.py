n = int(input("Enter n: "))
a, b = 0, 1
fib = []
for _ in range(n):
    fib.append(a)
    a, b = b, a + b
print("Fibonacci sequence:", fib)