n1 = 0
n2 = 5

for i in range(n2):
    n3 = int(input("Ingrese un numero: "))
    if n3 > n2:
        n2 = n3

print(n2)