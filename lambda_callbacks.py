def apply_operation(x, y, operation):
    return operation(x, y)

result = apply_operation(5, 3, lambda x, y: x * y)
print(result)
# Output: 15

