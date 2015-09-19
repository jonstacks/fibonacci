import itertools


def fibonacci():
    """
    A Generator for the fibonacci sequence
    """
    x0 = 0
    x1 = 1
    yield x0
    while True:
        n = x0 + x1
        yield n
        x1 = x0
        x0 = n


def fibonacci_n(n):
    """
    Returns an iterator for the first n numbers in the fibonacci sequence
    """
    if not isinstance(n, int):
        raise TypeError("Fibonacci sequence must be sliced with an int.")
    if n < 0:
        raise IndexError("Fibonacci sequence doesn't support negative slices")
    return itertools.islice(fibonacci(), n)
