# Recently discovered code with which we can configure the stack 
# that is RECURSION DEPTH of the program!  The sys module provides
# access to various variables and functions related to the Python 
# runtime environment. The default value is 1000 in python.
import sys
new_recursion_limit = 5000  # Set your desired recursion depth limit here

# Check the current recursion depth limit
current_recursion_limit = sys.getrecursionlimit()
print(f"Current recursion depth limit: {current_recursion_limit}")

# Set the new recursion depth limit
sys.setrecursionlimit(new_recursion_limit)
print(f"New recursion depth limit: {new_recursion_limit}")

# Let's see with an example, below code is of recursion with
# time complexity of O(2^n) & its stack will be looking as below
def generator(stringVal, limit):
    openCount = stringVal.count('(')
    closeCount = stringVal.count(')')
    
    if not limit:
        if openCount == closeCount:
            print(stringVal)
        elif openCount > closeCount:
            generator(stringVal + ')', limit)
    
    if openCount == closeCount and limit:
        generator(stringVal + '(', limit-1)
    elif openCount > closeCount and limit:
        generator(stringVal + '(', limit-1)
        generator(stringVal + ')', limit)

x = generator("", 3)

""" THIS IS A VERY SIMPLIFIED VIEW
+-------------------+
| Return Address   | <- Third Call
+-------------------+
| stringVal: "()"  |
| limit: 1         |
| openCount: 1     |
| closeCount: 1    |
+-------------------+
| Return Address   | <- Second Call
+-------------------+
| stringVal: "("   |
| limit: 2         |
| openCount: 1     |
| closeCount: 0    |
+-------------------+
| Return Address   | <- First Call
+-------------------+
| stringVal: ""    |
| limit: 3         |
| openCount: 0     |
| closeCount: 0    |
+-------------------+
| ...               |
|                   |
|                   |
+-------------------+
In each step the operating system allocates memory for another new
stack frame. The stack pointer is updated to point to the new stack frame.
"""