"""
Lesson 09.05: Indexing and Slicing in NumPy 
Course: Python Language Fundamentals - From Basics to AI Applications

Objective: 
Understand the techniques for indexing and slicing data in NumPy arrays.
""" 

import numpy as np

# ============================================================
# 1. Creating the basic structure with NumPy
# ============================================================
data_matrix = np.arange(1, 17, 1).reshape(4, 4)

print("=" * 50)
print("-" * 15 + " Original Matrix " + "-" * 16)
print(data_matrix)

"""
Note:
Before you create the data structure, you need to pay attention to its size. 
When you use np.arange(start, stop, step) with .reshape(), remember that 
arange creates a flat 1D vector of 'n' elements. You must ensure that 'n' 
can be perfectly fitted into the target matrix dimensions (e.g., 16 elements fit 4x4).
"""

# ============================================================
# 2. Accessing a specific row
# ============================================================
print("\n" + "=" * 50)
print("-" * 19 + " First Row " + "-" * 20)

first_row = data_matrix[0, :]
print(first_row)

"""
Note: 
To access the row we can use both syntaxes:
 - data_matrix[0]
 - data_matrix[0, :]
Performance is identical. The latter is often preferred for readability 
to explicitly show it is a 2D array.
"""

# ============================================================
# 3. Accessing a specific column
# ============================================================
print("\n" + "=" * 50)
print("-" * 18 + " First Column " + "-" * 18)

# Select all rows (:), but only the column at index 0
first_column = data_matrix[:, 0]
print(first_column)


# ============================================================
# 4. Accessing a specific interval (Submatrix)
# ============================================================
print("\n" + "=" * 50)
print("-" * 16 + " First 2x2 Subset " + "-" * 16)

# First two rows, first two columns
new_data_matrix = data_matrix[:2, :2]
print(new_data_matrix)


# ============================================================
# 5. Boolean Indexing: Selecting data based on a condition
# ============================================================
print("\n" + "=" * 50)
print("-" * 11 + " Boolean Indexing (Filters) " + "-" * 11)

elements_less_than = data_matrix[data_matrix < 7]
print(f"Elements less than 7:\n{elements_less_than}\n")

elements_bigger_than = data_matrix[data_matrix > 7]
print(f"Elements bigger than 7:\n{elements_bigger_than}")

"""
Note: 
Pay attention to this access method. The correct syntax is:
array[array_condition]
This creates a "boolean mask" under the hood and returns only the True values.
"""

# ============================================================
# 6. Advanced Slicing (start:stop:step)
# ============================================================
print("\n" + "=" * 50)
print("-" * 13 + " Advanced Stepped Slicing " + "-" * 13)

data_matrix_5x5 = np.arange(25).reshape(5, 5)
print(f"New 5x5 Matrix:\n{data_matrix_5x5}\n")

"""
Note:
We will use the step parameter in slicing (start:stop:step).
- Rows '::2' means: from beginning to end, stepping by 2 (indices 0, 2, 4).
- Columns '1::2' means: from index 1 to end, stepping by 2 (indices 1, 3).
"""

sliced_matrix = data_matrix_5x5[::2, 1::2]
print(f"Sliced Matrix:\n{sliced_matrix}")
print("=" * 50)
print("\n")