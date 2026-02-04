# Exercise 1.2
'''
Euclid showed that the greatest common divisor g(m, n) 
of two nonnegative integers m and n satisfies:

Write a Python function g(m,n) that employs recursion to calculate
the greatest common divisor of m and n using this formula.
Use your function to calculate and print 
the greatest common divisor of 108 and 192.
'''
def g(m, n):
    if n == 0:
        return m
    else:
        return g(n, m % n)

# Calculate GCD of 108 and 192
result = g(108, 192)
print(f"GCD of 108 and 192: {result}")
