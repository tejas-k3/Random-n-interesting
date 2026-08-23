"""
Late Binding Closures in Python

Why this is interesting:
A closure captures the variable, not a snapshot of its value.

The variable is looked up when the function is CALLED.

This is called "late binding".

The common surprise:

    lambda: i

does NOT remember the current value of `i`.
All functions refer to the same `i`, whose final value is 2.

The common fix:

    lambda i=i: i

Here, `i` is evaluated immediately and stored as the function's
default argument.

TODO:
- inspect `f.__closure__`
- inspect `f.__defaults__`
- understand closure cells
- experiment with `nonlocal`
"""


# ------------------------------------------------------------
# 1. Late binding
# ------------------------------------------------------------

functions = []

for i in range(3):
    # `i` is NOT copied into the lambda.
    # The lambda looks up `i` when it is called later.

    functions.append(lambda: i)


for f in functions:
    print(f())

# Expected output:
#
# 2
# 2
# 2


# Why?
#
# After the loop finishes:
#
#     i == 2
#
# All three functions refer to that same variable.
#
# Roughly:
#
#     function 1 ──┐
#     function 2 ──┼──> i == 2
#     function 3 ──┘


# ------------------------------------------------------------
# 2. Fixing late binding with a default argument
# ------------------------------------------------------------

functions = []

for i in range(3):
    # `i=i` evaluates the right-hand `i` NOW.
    #
    # Each function gets its own default value:
    #
    #     first  -> i = 0
    #     second -> i = 1
    #     third  -> i = 2

    functions.append(lambda i=i: i)


for f in functions:
    print(f())

# Expected output:
#
# 0
# 1
# 2


# ------------------------------------------------------------
# The important connection
# ------------------------------------------------------------
#
# lambda: i
#
#     "Look up i when I am called."
#
#
# lambda i=i: i
#
#     "Evaluate i now and store it as my default argument."
#
#
# This works because default arguments are evaluated when the
# function is CREATED, while the closure variable is looked up
# when the function is CALLED.
