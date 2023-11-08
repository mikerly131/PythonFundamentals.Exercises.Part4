# Program to figure out the x(n) given an n for the fibonacci sequence
# Must be done recursively, mathisfun is good reference for fibonnacci info


# Learning from factorial recursion, either the ns or the xs in the formual will be the recursive part
# if conditional so that when n is 0 or 1, it sets x to 0 or 1.  Seems making a recusive function keeps the variables from conflicting (x in this case)
def fibonacci(n):

    if (n == 0):
        x = 0
    elif (n == 1):
        x = 1
    else:
        x = fibonacci(n-1) + fibonacci(n-2)
    return x

user_input = input(f"Give me an integer, and I'll give you f(n) for the value in the Fibonnaci Sequence: ")
int_to_nocci = int(user_input)
ans = fibonacci(int_to_nocci)
print(f"f(n) =  {ans}")



# wrong, can't just drop the xs, or at least idk how to put it back in if I do yet, that seems mathy
#def getFibonacciValue(n):
#    x = (n - 1) + (n - 2)
#    return x



