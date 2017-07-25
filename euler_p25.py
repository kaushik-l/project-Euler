#Euler - problem 25
"""What is the index of the first term in the Fibonacci sequence to contain 1000 digits?"""

def fibonacci(term):
    if term == 1 or term == 2:
        return 1
    else:
        (f1, f2) = (1, 1)
        nterms = 2
        while nterms < term:
            f = f1 + f2
            (f1, f2) = (f2, f)
            nterms += 1
        return f2

term = 12
while len(str(fibonacci(term))) < 1000:
    term += 1

print term, fibonacci(term)
