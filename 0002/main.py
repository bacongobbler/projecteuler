def fibonacci(upper_limit=1000):
    sequence = [1, 2]
    while sequence[-1] < upper_limit:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence

if __name__ == '__main__':
    fib = fibonacci(4000000)
    sum = 0
    for v in fib:
        if v % 2 == 0:
            sum += v
    print(sum)