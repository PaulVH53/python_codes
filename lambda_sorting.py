students = [
    {'name': 'Alice', 'grade': 85},
    {'name': 'Bob', 'grade': 90},
    {'name': 'Charlie', 'grade': 80}
]
students_sorted = sorted(students, key=lambda x: x['grade'], reverse=True)
print(students_sorted)
# Output: [{'name': 'Bob', 'grade': 90}, {'name': 'Alice', 'grade': 85}, {'name': 'Charlie', 'grade': 80}]

