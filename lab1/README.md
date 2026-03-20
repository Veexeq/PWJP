# Lab 1: Mathematical Function Calculator

## Overview

This project is a command-line application developed for the first laboratory assignment. It serves as an interactive mathematical calculator utilizing the **SymPy** library for symbolic mathematics. The script allows users to evaluate various trigonometric and hyperbolic functions, as well as their first-order derivatives, at a given numerical point.

---

## Features

- **Trigonometric Functions**: Sine, Cosine, Tangent, Cotangent, Secant, Cosecant.
- **Hyperbolic Functions**: Sinh, Cosh, Tanh, Coth.
- **Symbolic Differentiation**: Calculates the first derivative of any supported function on the fly by appending a simple suffix.
- **Robust Input Validation**: Handles invalid user inputs, non-numeric strings, and empty submissions.
- **Mathematical Edge Cases**: Safely catches evaluation errors such as division by zero (e.g., evaluating cotangent at zero).

---

## Requirements

- **Python 3.x**
- **SymPy** library

To install the required dependencies, activate your virtual environment and run:

```bash
pip install -r requirements.txt
```

---

## Usage

Run the script from your terminal:

```bash
python mini_projekt.py
```

### Example Interaction

1. The program will display a list of available functions with corresponding IDs.
2. Enter the **number** corresponding to the desired function.
3. To evaluate the **first derivative**, append the letter **`f`** to the number (e.g., `4f` for the derivative of the cotangent function).
4. Provide a numerical argument for evaluation.

**Sample Output:**

```text
Proszę wybrać funkcję lub jej pochodną poprzez jej numer: 4f
Podaj argument funkcji: 2
Wybrany wzór matematyczny: y = -cot(x)**2 - 1
Wynik: -1.045
```