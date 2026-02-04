# Exercise 1.1
'''
Write a function that checks if a number is prime and 
print out 100 prime numbers after some given number n.
The number n must be provided by a user.
'''
def is_prime(n):
    if n < 2:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n**0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

n = int(input("Enter a number: "))
count = 0
current = n + 1

while count < 100:
    if is_prime(current):
        print(current, end=" ")
        count += 1
    current += 1