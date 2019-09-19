import numpy as np


# Users can add functions to be tested here.
def f3(x):
    f = x
    return f


# Certain functions may have to be integrated before putting them into the Riemann Sum Calculator
def f2(x):
    f = (2 * np.pi) * (x * (9.0 - x ** 2))
    return f


# function problem #2
def f1(x):
    f = np.e ** (-x ** 2)
    return f


# My Riemann Sum Calculator
def Riemann(f, a, b, error):
    integral = 0
    step_size = error

    # If a is bigger then b swap them
    if a > b:
        a, b = b, a

    x = a
    while x < b:
        area = f(x) * step_size
        integral = integral + area
        x = x + step_size
    return integral


# Print out the results for your function
print("The volume of Problem #1 is:")
print(Riemann(f2, 2, 3, .000001))
print("\nThe volume of problem #2 is:")
print(Riemann(f1, 0, 2, .000001))


# e = eval('lambda x, y: ' + raw_input('enter equation for y=f(x): '))
# THE EVAL FUNCTION IS VERY FINICKY. PROPER "NUMPY SYNTAX" & PYTHON MUST BE USED FOR IT TO WORK.
# ONLY USE 'x' as a variable in your function.
# "PEBKAC" HIGHLY POSSIBLE...
userFunction = eval('lambda x: ' + input('\nEnter your equation using proper numpy syntax: '))
# Proper Syntax Example --> (2 * np.pi) * (x * (9.0 - x ** 2))
userLowerBound = eval(input("Please provide your lower bound (a): "))
userUpperBound = eval(input("Please provide your upper bound (b): "))
userError = eval(input("Please provide error (ex.  .0001 or .0000001, etc): "))

print("\nThe volume of user problem is:")
print(Riemann(userFunction, userLowerBound, userUpperBound, userError))
