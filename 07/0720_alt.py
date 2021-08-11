import string

alpha = string.printable[36:]

n = 3
for i in range(0, len(alpha), n):
    print(alpha[i:i + n])
    n -= 1
    if n == 0:
        break
