import numpy as np

def f(x):
    return (np.sin(np.sqrt(100 * x)))**2

# --- (a) Adaptive Trapezoidal Rule ---
print("=" * 60)
print("Exercise 5.7(a): Adaptive Trapezoidal Rule")
print("=" * 60)
print(f"{'N':>6} {'Integral':>15} {'Error Estimate':>15}")
print("-" * 60)

a, b = 0, 1
eps = 1e-6
n = 1
h = b - a
I_old = 0.5 * h * (f(a) + f(b))
print(f"{n:6d} {I_old:15.10f} {'---':>15}")
error = 1.0

while error > eps:
    n *= 2
    h /= 2
    # Add only the new points (odd indices)
    s = sum(f(a + i * h) for i in range(1, n, 2))
    I_new = 0.5 * I_old + h * s
    
    error = abs(I_new - I_old) / 3.0
    print(f"{n:6d} {I_new:15.10f} {error:15.10f}")
    I_old = I_new

print("=" * 60)
print(f"Final Result: I = {I_new:.10f}\n")

# --- (b) Romberg Integration ---
print("=" * 60)
print("Exercise 5.7(b): Romberg Integration")
print("=" * 60)
print("Triangular table of Romberg estimates:")
print()

# Store the full table for display
romberg_table = []
R = [0.5 * (b - a) * (f(a) + f(b))]
romberg_table.append(R[:])
print(f"N=1:  {R[0]:15.10f}")

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
    romberg_table.append(R[:])
    
    # Print the row
    row_str = f"N={n:<3}: "
    row_str += "  ".join(f"{val:15.10f}" for val in R)
    print(row_str)

print("=" * 60)
print(f"Final Result: I = {R[-1]:.10f}\n")
