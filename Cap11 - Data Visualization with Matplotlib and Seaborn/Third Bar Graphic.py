import matplotlib.pyplot as plt

ages  = [22,65,45,21,22,34,42,4,99,101,120,122]

ids  = [x for x in range(len(ages))]

plt.bar(ids,ages)
plt.title("People age")
plt.show()

