"""
Lesson 09.04: Data Types in the NumPy Library
Course: Python Language Fundamentals - From Basics to AI Applications

Objective: 
Understand the main data types within the NumPy library and how to convert them.
""" 

import numpy as np

"""
Note: 
Unlike standard Python lists, NumPy arrays are homogeneous. This means that all 
elements must be of the same data type. This is crucial for performance and memory efficiency.
"""

# ============================================================
# 1. NumPy infers the datatype automatically
# ============================================================

# Integer
arr_integer = np.array([1, 2, 3])

print("=" * 50)
print("-" * 20 + " Int " + "-" * 20)
print(f"Array:\n{arr_integer}")
print(f"Data type: {arr_integer.dtype}")
print("=" * 50)


# Float
arr_float = np.array([1.0, 2.0, 3.0])

print("\n" + "=" * 50)
print("-" * 20 + " Float " + "-" * 20)
print(f"Array:\n{arr_float}")
print(f"Data type: {arr_float.dtype}")
print("=" * 50)


# ============================================================
# 2. NumPy allows us to define the datatype during creation
# ============================================================

new_arr_int = np.array([1, 2, 3, 4, 5], dtype=np.int16)

print("\n" + "=" * 50)
print("-" * 15 + " Defining int16 " + "-" * 15)
print(f"Array:\n{new_arr_int}")
print(f"Data type: {new_arr_int.dtype}")
print("-" * 50)

# Changing the data type
arr_int_to_float = new_arr_int.astype(np.float16)

print(f"Converted Array:\n{arr_int_to_float}")
print(f"New Data type: {arr_int_to_float.dtype}")
print("=" * 50)


# ============================================================
# 3. Changing datatype and memory size during execution
# ============================================================

new_arr_float32 = np.array([1.5, 2.5, 3.5, 4.5, 5.5], dtype=np.float32)

print("\n" + "=" * 50)
print("-" * 15 + " Float32 to Int16 " + "-" * 15)
print(f"Array:\n{new_arr_float32}")
print(f"Data type: {new_arr_float32.dtype}")
print("-" * 50)

# Notice how converting float to int truncates the decimal values!
arr_float32_to_int16 = new_arr_float32.astype(np.int16)

print(f"Converted Array:\n{arr_float32_to_int16}")
print(f"New Data type: {arr_float32_to_int16.dtype}")
print("=" * 50)
print("\n")


"""
Memory Note: 
In NumPy, we have different sizes of integers and floats (8, 16, 32, 64 bits).
This means we can create a variable with more or less memory space depending on our needs.

Standard sizes:
- int8, int16, int32, int64
- float16, float32, float64

Execution Note: 
If you just perform something like:
`new_arr_float32.astype(np.int16)`
without saving the result in a local variable, you won't visualize the change. 
You need to save it to a new variable (or overwrite the existing one) to use it later.
"""