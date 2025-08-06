a = 0
b = 1
c = 0
print(a, b, end=" ")

for i in range(3, 16):
    c = b + a
    print(c, end=" ")
    a = b
    b = c