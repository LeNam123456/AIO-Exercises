def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result
sin = lambda x, n: [(-1) ** i * (x ** (2 * i + 1) / factorial(2 * i + 1)) for i in range(n)]
cos = lambda x, n: [(-1) ** i * (x ** (2 * i) / factorial(2 * i)) for i in range(n)]
tan = lambda x, n: [x ** (2 * i + 1) / factorial(2 * i + 1) for i in range(n)]
cosh = lambda x, n: [x ** (2 * i) / factorial(2 * i) for i in range(n)]

x = 3.14
n = int(input("Enter n:"))

print(sum(sin(x, n)))
print(sum(cos(x, n)))
print(sum(tan(x, n)))
print(sum(cosh(x, n)))