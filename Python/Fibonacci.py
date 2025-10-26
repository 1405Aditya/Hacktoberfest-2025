# Iterative
def fibonacci(n):
    sequence = [0, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence[:n]

n = 10
print("Fibonacci Sequence:", fibonacci(n))
