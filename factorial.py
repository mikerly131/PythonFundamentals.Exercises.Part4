# Program to calculate the factorial value of user given X, where X is int from 0 to 995
# I learned the factorial formual from Mathisfun.com 

# Function to get user input, int X
def get_user_integer():
    user_integer = input("I will give you a factorial.  First, you give me an integer between from 0 up to 995: ")
    return user_integer

# Recursive function to determine factorial of int X. Need to set ans to 1 if x is 1, otherwise it won't work, trust me.
def factorial(x):

    if (x == 1):
        ans = 1
    elif (x > 1):
        ans = x * factorial(x-1)
    
    return ans

# Control Flow - get user input, convert to int, do factorial, print answer
user_input = get_user_integer()
int_to_factorial = int(user_input)
answer = factorial(int_to_factorial)
print(f"The total is: {answer}")

