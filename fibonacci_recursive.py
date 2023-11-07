"""
**Requirements**

* Given a term (n), determine the value of x(n).
* In the *fibonacci_recursive.py* program, create a function called *fibonnaci*. 
The function should take in an integer and return the value of x(n).
* This problem must be solved using recursion. 
"""


def getFibonacciValue(n):
    x = (n - 1) + (n - 2)
    return x

print(getFibonacciValue(9))


