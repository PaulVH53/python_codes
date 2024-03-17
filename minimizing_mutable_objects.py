from collections import namedtuple

# Define a namedtuple for representing a point
Point = namedtuple('Point', ['x', 'y'])

# Create a list of Point instances
points = [Point(x=1, y=2) for _ in range(10000)]

