import numpy as np

def f(x):
    return (np.sin(np.sqrt(100 * x)))**2

# --- (a) Adaptive Trapezoidal Rule ---
a, b = 0, 1
eps = 1e-6
n = 1
h = b - a
I_old = 0.5 * h * (f(a) + f(b))
error = 1.0

while error > eps:
    n *= 2
    h /= 2
    # Add only the new points (odd indices)
    s = sum(f(a + i * h) for i in range(1, n, 2))
    I_new = 0.5 * I_old + h * s
    
    error = abs(I_new - I_old) / 3.0
    I_old = I_new

print(f"Trapezoidal Result: {I_new:.6f} using {n} slices")

# --- (b) Romberg Integration ---
# We use a 1D list 'R' to store only the current row of the Romberg table
R = [0.5 * (b - a) * (f(a) + f(b))]
n = 1
h = b - a
error = 1.0

while error > eps:
    n *= 2
    h /= 2
    s = sum(f(a + i * h) for i in range(1, n, 2))
    trap_estimate = 0.5 * R[0] + h * s
    
    new_row = [trap_estimate]
    for m in range(1, len(R) + 1):
        # The Romberg formula (Richardson Extrapolation)
        prev_m = new_row[m-1]
        above_m = R[m-1]
        extrapolated = prev_m + (prev_m - above_m) / (4**m - 1)
        new_row.append(extrapolated)
    
    error = abs(new_row[-1] - R[-1])
    R = new_row

print(f"Romberg Result:     {R[-1]:.6f} using {n} slices")
