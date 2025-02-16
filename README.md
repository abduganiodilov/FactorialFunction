# Factorial Function in Python

![Python](https://img.shields.io/badge/Python-3.x-blue.svg) ![Recursive Function](https://img.shields.io/badge/Recursion-Enabled-green.svg)

## 📌 Overview
This repository contains a simple yet powerful Python function to compute the factorial of a given number using **recursion**. The function ensures that only non-negative integers are accepted and implements **error handling** using assertions.

## 📝 Code Explanation
```python
def factorial(n):  
    assert n >= 0, "Factorial must be greater than or equal to 0"  
    if n == 0:  
        return 1  
    return n * factorial(n-1)  

print(factorial(5))  
```

🔹 **Recursive Function**: Calls itself with `n-1` until reaching the base case.
🔹 **Base Case**: When `n == 0`, returns `1` (since `0! = 1`).
🔹 **Assertion Check**: Ensures the input is a non-negative integer.

---

## 🚀 How to Run
1. Install Python (if not already installed) 👉 [Download Python](https://www.python.org/downloads/)
2. Copy and paste the code into a Python file (e.g., `factorial.py`).
3. Run the script:
   ```bash
   python factorial.py
   ```
4. You should see the output:
   ```
   120
   ```

---

## 📖 Example Usage
```python
print(factorial(3))  # Output: 6
print(factorial(5))  # Output: 120
print(factorial(0))  # Output: 1
```

---

## ⚠️ Error Handling
If a negative number is provided, the assertion will raise an error:
```python
print(factorial(-2))  # AssertionError: Factorial must be greater than or equal to 0
```

---

## 🛠 Applications
✔️ **Mathematical Computations**
✔️ **Combinatorics and Probability**
✔️ **Algorithm and Data Structures**
✔️ **Computer Science & Competitive Programming**

---

## 📌 Contributing
Feel free to submit issues and pull requests if you find any improvements or additional features to add!

---

## 📝 License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

