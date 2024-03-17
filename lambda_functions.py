# Using map() with lambda
numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(squared)
# Output: [1, 4, 9, 16, 25]

# Using filter() with lambda
numbers = [1, 2, 3, 4, 5]
even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)
# Output: [2, 4]

# Using reduce() with lambda
from functools import reduce
total = reduce(lambda x, y: x + y, numbers)
print(total)
# Output: 15

