"""
Serie de Fibonacci.
"""
num = int(input("Ingresa un número: "))

fib_series = [0, 1]
while fib_series[-1] + fib_series[-2] < num:
    fib_series.append(fib_series[-1] + fib_series[-2])

print(f"Serie de Fibonacci hasta {num}: {fib_series}")
