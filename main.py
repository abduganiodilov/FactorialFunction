def factorial(n):
    # Define a function named 'factorial' that takes one argument 'n'

    assert n >= 0, "Factorial must be greater than or equal to 0"
    # Ensure 'n' is a non-negative integer; otherwise, raise an assertion error with a message

    if n == 0:
        # Base case: if 'n' is 0, return 1 since 0! is defined as 1
        return 1

    return n * factorial(n - 1)
    # Recursive case: multiply 'n' by the factorial of (n-1) until reaching the base case


print(factorial(5))
# Call the 'factorial' function with an argument of 5 and print the result
