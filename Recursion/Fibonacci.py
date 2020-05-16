# Fibonacci numbers using Linear Recursion.
# return pair of Fibonacci (f(n) and f(n-1)).
def fibonacci(n):
    if n <= 1:
        return (n,0)
    else:
        (a,b) = fibonacci(n-1)
        return (a+b, a)

print(fibonacci(4))
