"""
Lesson 09.01: Comparing Performance - Numpy vs. Pure Python
Course: Python Language Fundamentals - From Basics to AI Applications

Objectives: 
Demonstrate the speed and efficiency of Numpy arrays compared to 
standart Python listis when performing leage-scale numerical operations
"""

import time
import math
import numpy as np

#1. Data Prepration
#Using an underscore (_) in large numbers makes them much easier to read
prices_np = np.random.rand(10_000_000)
prices_list  = list(prices_np)

print("-"*50)
print(f"Data type of 'prices_np':{type(prices_np)}")
print(f"Data type of 'prices_list':{type(prices_list)}")
print("-"*50)
print("\n")

# ==========================================
# 2. Performing operations with NumPy
# ==========================================
t0 = time.time()

#Operations applied to the entire array at once (Vectorization)
discount = prices_np*0.90
final_price  = discount + 5
sqrt = np.sqrt(prices_np)

time_numpy = time.time() - t0
print(f"Execution time with Numpy: {time_numpy:.4f} seconds!")
#The spended time with Numpy: 0.4300 seconds!

# ==========================================
# 3. Performing operations with Pure Python
# ==========================================


t1 = time.time()

##Operations applied element by element using list Comprehensions
discount = [p *0.98 for p in prices_list]
final_price = [p + 5 for p in discount]
sqrt = [math.sqrt(p) for p in prices_list]

time_list_comprehencions = time.time() - t1
print(f"Execution time with list comprehensions: {time_list_comprehencions:.4f} seconds!\n")
#The spended time with Python Lists: 5.8466267585754395 seconds!

#Performance multiplier
print("-"*50)
print(f"Numpy was {(time_numpy / time_list_comprehencions)*100:.2f}x faster!")
print("-"*50)
print("\n")




