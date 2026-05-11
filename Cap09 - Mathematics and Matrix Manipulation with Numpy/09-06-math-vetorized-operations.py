"""
Lesson 09.06: math vetorized operations
Course: Python Language Fundamentals - From Basics to AI Applications

Objective: 
Implement techniques to perform math vectorized operations in data structure in NumPy arrays.
""" 

import numpy as np 
import time

# ============================================================
# 1. Simulate three studantes score of four exames
# ============================================================

exam_score  = np.array([
    [8.5,7.0,9.2,6.5],
    [5.5,6.8,7.5, 8.0],
    [9.5,9.0,8.8,10.0] 
    ])

print("=" * 50)
print("-" * 15 + " Examem score data set " + "-" * 16)
print(f"{exam_score}\n")
print(f"Type: {type(exam_score)}")
print("\n")

# ============================================================
# 2. Matrix agregation
# ============================================================

print("=" * 50)
print("-" * 15 + " Matrix Agregation " + "-" * 16)
print(f"General Average:{exam_score.mean():.2f}")
print(f"Max Score: {exam_score.max()}")
print(f"Min Score: {exam_score.min()}")
print(f"Sum Score: {exam_score.sum()}")
print("\n")


# ============================================================
# 3. Axis agregation
# ============================================================

"""
Calculate the mean of each studant (agregation of columns, axis = 1)
Rouding by two decimal places
"""

studant_average = exam_score.mean(axis = 1).round(2)
print("=" * 50)
print("-" * 15 + " Axis Agregation " + "-" * 16)
print(f"Studant Average:{studant_average}")
print("\n")


# ============================================================
# 3. Line agregation
# ============================================================

"""
Calculate the mean of each studant (agregation of columns, axis = 1)
Rouding by two decimal places
"""

average_by_exam = exam_score.mean(axis = 0).round(2)
print("=" * 50)
print("-" * 15 + " Line Agregation " + "-" * 16)
print(f"Exman Average:{average_by_exam}")
print("\n")

