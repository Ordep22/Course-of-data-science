"""
[PT]

[EN]

zip() returns an iterator of tuples, where the i-th tuple contains t
he i-th element from each of the argument iterables.
"""

listOne = [1,3,5,7]
listTwo= [2,4,6,8]

zipResult = zip(listOne,listTwo)

listResult = list(zipResult)

print(f"The iterable objetc is: {zipResult}")

print(f"The new list is: {listResult}")



