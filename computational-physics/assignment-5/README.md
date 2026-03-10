# Assignment 5

Newman, *Computational Physics* (2012), Exercises 5.7 & 5.8

## Problem

Evaluate: $I = \int_0^1 \sin^2(\sqrt{100x}) \, dx$ with accuracy $\varepsilon = 10^{-6}$

Analytical result: $I \approx 0.45583$

---

## Exercise 5.7(a): Adaptive Trapezoidal Rule

Uses Eq. 5.34 with error estimate $\varepsilon \approx |I_{new} - I_{old}|/3$

**Output:**
```
     N        Integral  Error Estimate
------------------------------------------------------------
     1    0.1479794845             ---
     2    0.3252319078    0.0590841411
     4    0.5122828507    0.0623503143
     8    0.4029974485    0.0364284674
    16    0.4301033693    0.0090353069
    32    0.4484146658    0.0061037655
    64    0.4539129312    0.0018327551
   128    0.4553485044    0.0004785244
   256    0.4557112665    0.0001209207
   512    0.4558021997    0.0000303111
  1024    0.4558249481    0.0000075828
  2048    0.4558306362    0.0000018960
  4096    0.4558320583    0.0000004740

Final Result: I = 0.4558320583
```

**Answer:** I = 0.45583 (requires 4096 slices)

---

## Exercise 5.7(b): Romberg Integration

Uses Eq. 5.49 with Richardson extrapolation. Shows triangular table of estimates.

**Output (triangular table):**
```
N=1:     0.1479794845
N=2  :    0.3252319078     0.3843160489
N=4  :    0.5122828507     0.5746331650     0.5873209728
N=8  :    0.4029974485     0.3665689811     0.3526980355     0.3489738619
N=16 :    0.4301033693     0.4391386762     0.4439766559     0.4454255229     0.4458037647
N=32 :    0.4484146658     0.4545184313     0.4555437483     0.4557273529     0.4557677523     0.4557774922
N=64 :    0.4539129312     0.4557456864     0.4558275034     0.4558320074     0.4558324178     0.4558324810     0.4558324945
N=128:    0.4553485044     0.4558270288     0.4558324516     0.4558325301     0.4558325322     0.4558325323     0.4558325323     0.4558325323

Final Result: I = 0.4558325323
```

**Answer:** I = 0.45583 (requires only 128 slices, 32× faster than trapezoidal)

---

## Exercise 5.8: Adaptive Simpson's Rule

Uses Eq. 5.36: $S_{2N} = (4T_{2N} - T_N)/3$ starting with N=2

**Output:**
```
     N     Simpson Estimate  Error Estimate
------------------------------------------------------------
     2         0.3843160489             ---
     4         0.5746331650    0.0126878077
     8         0.3665689811    0.0138709456
    16         0.4391386762    0.0048379797
    32         0.4545184313    0.0010253170
    64         0.4557456864    0.0000818170
   128         0.4558270288    0.0000054228
   256         0.4558321871    0.0000003439

Final Result: I = 0.4558321871
```

**Answer:** I = 0.45583 (requires 256 slices, 16× faster than trapezoidal)

---

## Summary

| Method | Result | Slices | Relative Efficiency |
|--------|--------|--------|---------------------|
| Trapezoidal | 0.4558320583 | 4,096 | 1× (baseline) |
| Simpson's | 0.4558321871 | 256 | 16× faster |
| Romberg | 0.4558325323 | 128 | 32× faster |

All methods converge to the analytical result I ≈ 0.45583
