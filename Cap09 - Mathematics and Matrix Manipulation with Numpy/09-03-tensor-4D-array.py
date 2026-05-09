"""
Lesson 09.03: Creating Tensors using NumPy Arrays  
Course: Python Language Fundamentals - From Basics to AI Applications

Objective: 
Demonstrate how to create 4D arrays (tensors) using NumPy 
and inspect their main attributes such as shape, ndim, and size.
"""

import numpy as np

# ============================================================
# 1. Creating a 4-Dimensional Array (Tensor) using np.arange() 
# ============================================================
"""
Note: 
4D array with sequential values from 0 to 119 organized in a 
2x3x4x5 shape (2 blocks, 3 depth/planes, 4 rows, 5 columns).
"""
tensor_4d = np.arange(120).reshape(2, 3, 4, 5)

print("=" * 50)
print("Tensor (4D Array):\n")
# Printing the entire tensor to visualize its nested structure
print(tensor_4d)
print("=" * 50)


# ============================================================
# 2. Checking the Tensor attributes
# ============================================================
# For 4D, the shape represents (blocks/batches, depth, rows, columns)
print(f"Tensor shape (blocks, depth, rows, columns): {tensor_4d.shape}") 
print(f"Number of dimensions (ndim): {tensor_4d.ndim}") 
print(f"Tensor size (number of elements): {tensor_4d.size}") 
print("=" * 50)
print("\n")