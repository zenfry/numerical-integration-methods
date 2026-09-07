#Numerical Integration Methods

- Implements Riemann sums (midpoint), trapezoidal rule, and Simpson's rule from scratch, no scipy.integrate
- Simpson's rule fits parabolas per interval vs. lines for trapezoidal, giving O(h⁴) vs O(h²) convergence
- Error verified against known exact values for x² and sin(x), and against erf-based reference for e^(-x²), a function with no elementary antiderivative
- Convergence confirmed empirically: Simpson's error shrinks ~16x per doubling of n, trapezoidal ~4x
