# Exercise 1.3
'''
A ball is dropped from a tower of height h with initial velocity zero.
Write a program that asks the user to enter the height in meters of
the tower and then calculates and prints the time the ball takes until
it hits the ground, ignoring air resistance. Use your program 
to calculate the time for a ball dropped from a 100 m high tower.
(Hint: Find the formula for a free-falling object.)
'''
import math

h = float(input("Enter the height in meters: "))
g = 9.81

t = math.sqrt(2 * h / g)

print(f"Time to hit the ground: {t:.2f} seconds")