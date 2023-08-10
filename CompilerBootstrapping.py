# Step 1: Initial Compiler (Python code)
def initial_compiler(source_code):
    intermediate_code = compile(source_code, filename='', mode='exec')
    return intermediate_code

# Step 2: Stage 1 Compilation
source_code = "print('Tejas')"
intermediate_code = initial_compiler(source_code)

# Step 3: Stage 1 Execution
exec(intermediate_code)

# Step 4: Stage 2 Compilation
optimized_intermediate_code = initial_compiler(source_code)

# Step 5: Stage 2 Execution
exec(optimized_intermediate_code)

# Step 6: Intermediate Compiler (Python code)
def intermediate_compiler(intermediate_code):
    optimized_code = compile(intermediate_code, filename='', mode='exec')
    return optimized_code

# Step 7: Stage 3 Compilation
intermediate_code = "print('Tejas')"
optimized_code = intermediate_compiler(intermediate_code)

# Step 8: Stage 3 Execution
exec(optimized_code)

# Step 9: Final Compiler (Python code)
def final_compiler(optimized_code):
    final_code = compile(optimized_code, filename='', mode='exec')
    return final_code

# Step 10: Stage 4 Compilation and Execution
final_code = final_compiler(optimized_code)
exec(final_code)

"""
exec() Function:

The exec() function in Python is used to dynamically execute a block of Python code (represented as a string).
It takes a single argument, which is the Python code to be executed.
In the code snippet, exec() is used to execute the compiled intermediate and optimized code, as well as the final code.
Compiler Function:

In the code snippet, there are three compiler functions: initial_compiler(), intermediate_compiler(), and final_compiler().
These functions simulate the stages of compilation.
Each compiler function takes a block of Python source code as input and compiles it into bytecode (an intermediate form of code that is executed by the Python interpreter).
In practice, these compiler functions would involve more complex processes, including lexical analysis, parsing, semantic analysis, and code generation.
compile() Function:

The compile() function is a built-in Python function used to compile Python source code into bytecode or code objects.
It takes three arguments: the source code as a string, a filename (which can be an empty string), and the mode of compilation (such as 'exec' for a sequence of statements).
In the code snippet, compile() is used within the compiler functions to transform source code into intermediate, optimized, and final code.
source_code:

This variable holds the Python source code that needs to be compiled and executed.
In the code snippet, source_code contains the code "print('Tejas')", which prints the string 'Tejas' when executed.
intermediate_code, optimized_code, final_code:

These variables store the compiled code at different stages of the bootstrapping process.
intermediate_code holds the intermediate representation of the source code after the initial compilation.
optimized_code holds the optimized version of the intermediate code after further compilation.
final_code holds the final version of the code after compilation using the self-hosted compiler.
Remember that this code snippet is a simplified representation to illustrate the bootstrapping process, and real-world compilers are more complex, involving multiple stages of analysis and transformation.
"""