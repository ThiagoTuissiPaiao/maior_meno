n1 = int(input("Primeiro numero: "))
n2 = int(input("Segundo numero: "))
n3 = int(input("Terceiro numero: "))

bigger = n1
if n2 > bigger:
    bigger = n2
if n3 > bigger:
    bigger = n3

print(f"Maior: {bigger}")

smaller = n1
if n2 < smaller:
    smaller = n2
if n3 < smaller:
    smaller = n3

print(f"Menor: {smaller}")
