# Assignment 5

Newman, *Computational Physics* (2012), Exercises 5.7 & 5.8

## Problem

Evaluate: $I = \int_0^1 \sin^2(\sqrt{100x}) \, dx$ with accuracy $\varepsilon = 10^{-6}$

Analytical result: $I \approx 0.45583$

## Exercise 5.7

**(a) Adaptive Trapezoidal Rule (Eq. 5.34)**

```
Trapezoidal Result: 0.455832 using 4096 slices
```

**(b) Romberg Integration (Eq. 5.49)**

```
Romberg Result: 0.455833 using 128 slices
```

## Exercise 5.8

**Adaptive Simpson's Rule (Eq. 5.36)**

```
Simpson's Result: 0.45583219
Number of Slices: 256
```

## Results

| Method | Result | Slices |
|--------|--------|--------|
| Trapezoidal | 0.455832 | 4,096 |
| Simpson's | 0.45583219 | 256 |
| Romberg | 0.455833 | 128 |

Romberg is most efficient (32× faster than trapezoidal), followed by Simpson's (16× faster).
