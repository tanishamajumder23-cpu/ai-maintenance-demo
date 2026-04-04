def calculate(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Both inputs must be numbers")
    return a + b

result = calculate(5, 10)
print(result)