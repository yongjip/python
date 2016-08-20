# Recursively
def fibonacci(position):
    if position == 0 or position == 1:
        return position
    return fibonacci(position - 1) + fibonacci(position - 2)

# For loop. Much faster than recursive
def fibonacci(position):
    if position == 0:
        return 0
    elif position == 1:
        return 1
    first = 0
    second = 1
    for i in range(position):
        out = first + second
        first = second
        second = out
    return out
