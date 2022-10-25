import collections
de = collections.deque([1, 2, 3])
print("deque: ", de)
de.append(4)
print("\nThe deque after appending at right is : ")
print(de)
de.appendleft(6)
print("\nThe deque after appending at left is : ")
print(de)
