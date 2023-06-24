def fibonacci(n):
    x = 1
    n1 = 0
    n2 = 1
    while x < n:
        result = n1 + n2
        temp = n2
        n1 = temp
        n2 = result
        x += 1
    return result

print(fibonacci(6))