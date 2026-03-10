import numpy as np

def f(x):
    return (np.sin(np.sqrt(100 * x)))**2

# Parameters
a, b = 0, 1
eps = 1e-6

# Initial setup: Start with N=1 to get T_1, then N=2 to get S_2
n = 1
h = b - a
T_old = 0.5 * h * (f(a) + f(b))

# Move to N=2 (the starting point requested)
n = 2
h = h / 2
s_odd = f(a + h) # Only one odd point at x=0.5
T_new = 0.5 * T_old + h * s_odd
S_old = (4 * T_new - T_old) / 3

error = 1.0

# Adaptive Loop
while error > eps:
    T_old = T_new
    n *= 2
    h /= 2
    
    # Calculate T_2N using Eq. 5.34
    s_odd = sum(f(a + i * h) for i in range(1, n, 2))
    T_new = 0.5 * T_old + h * s_odd
    
    # Calculate S_2N using Eq. 5.36
    S_new = (4 * T_new - T_old) / 3
    
    # Error estimate using Richardson extrapolation for Simpson's
    error = abs(S_new - S_old) / 15.0
    S_old = S_new

print(f"Simpson's Result: {S_new:.8f}")
print(f"Number of Slices: {n}")
