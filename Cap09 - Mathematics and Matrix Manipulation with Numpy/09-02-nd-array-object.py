"""
Lesson 09.02: Creating NumPy Arrays and Checking Attributes
Course: Python Language Fundamentals - From Basics to AI Applications

Objective: 
Demonstrate how to create 1D (vectors), 2D (matrices), and 3D (tensors) arrays 
using NumPy and inspect their main attributes such as shape, ndim, and size.
"""

import numpy as np

# ============================================================
# 1. Creating a 1-Dimensional Array (Vector) from a list
# ============================================================
data = [1, 2, 3, 4, 6]
vector = np.array(data)

print("=" * 50)
print("Vector (1D Array):\n")
print(vector)
print("=" * 50)


# ============================================================
# 2. Checking the Vector attributes
# ============================================================
print(f"Vector shape: {vector.shape}")
print(f"Number of dimensions (ndim): {vector.ndim}")
print(f"Vector size (number of elements): {vector.size}")
print("=" * 50)


# ============================================================
# 3. Creating a 2-Dimensional Array (Matrix) from a list of lists
# ============================================================
matrix = np.array([[1, 2, 3], [4, 5, 6]])

print("\nMatrix (2D Array):\n")
print(matrix)
print("=" * 50)


# ============================================================
# 4. Checking the Matrix attributes
# ============================================================
print(f"Matrix shape (rows, columns): {matrix.shape}")
print(f"Number of dimensions (ndim): {matrix.ndim}") 
print(f"Matrix size (number of elements): {matrix.size}") 
print("=" * 50)


# ============================================================
# 5. Creating a 3-Dimensional Array (Tensor) using np.arange()
# ============================================================
"""
Note:
The main difference between np.array() and np.arange() is that np.array() builds 
an array from existing data like a list. On the other hand, np.arange() builds an 
array from a numerical sequence (e.g., an array with 24 elements). 

To convert this flat sequence into a 3D tensor, we must use the .reshape() method.
"""

arr = np.arange(24).reshape(4, 3, 2)

print("\nTensor (3D Array):\n")
print(arr)
print("=" * 50)


# ============================================================
# 6. Checking the Tensor attributes
# ============================================================
print(f"Tensor shape (depth, rows, columns): {arr.shape}") 
print(f"Number of dimensions (ndim): {arr.ndim}") 
print(f"Tensor size (number of elements): {arr.size}") 
print("=" * 50)
print("\n")