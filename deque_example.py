from collections import deque

# Create a deque
d = deque([1, 2, 3, 4, 5])
print(d)

# Efficient insertions at both ends
d.appendleft(0)   # Insert at the beginning
print(d)
d.append(6)       # Insert at the end
print(d)

# Efficient deletions at both ends
#  These operations have constant time complexity, O(1), regardless of the deque's size.
left_item = d.popleft()  # Remove from the beginning
right_item = d.pop()     # Remove from the end

print(d)  # Output: deque([1, 2, 3, 4, 5])
print(left_item, right_item)  # Output: 0 6


# Avoiding Lists for Frequent Insertions or Deletions in the Middle:

# Using a list for frequent insertions or deletions in the middle
lst = [1, 2, 3, 4, 5]
print(lst)

# Inefficient insertion in the middle
# These operations have time complexity of O(n), where n is the size of the list, as elements need to be shifted to accommodate the changes.
lst.insert(2, 10)  # Insert 10 at index 2
print(lst)

# Inefficient deletion in the middle
del lst[2]  # Delete item at index 2
print(lst)  # Output: [1, 2, 4, 5]