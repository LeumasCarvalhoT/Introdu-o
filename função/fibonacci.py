i = 0
t1 = 0
t2 = 1
print(t1, t2, end=' ')

def fibonacci(n1, n2):
    for i in range(1, 14):
        n3 = n1 + n2
        n1 = n2
        n2 = n3
        print(n3, end=' ')
    return n3

t3 = fibonacci(t1, t2)
