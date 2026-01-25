import random
N = int(input("Määrä"))
n = 0
numero = 0
while numero < N:
    x = random.randint(-1,1)
    y = random.randint(-1,1)
    if x*x + y*y<1:
        n = n + 1
    numero  = numero + 1
pii = 4 * n/N
print("pii on noin;" , pii)
