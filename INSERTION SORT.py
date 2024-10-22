# INSERTION SORT
N = int(input("Ingrese la cantidad de elementos del Array: "))
Array = []

for i in range(N):
    n = int(input(f"Ingrese el valor {i+1}: "))
    Array.append(n)

print("El Array original es: ")
for i in range(N):
    print(Array[i], end=" ")
print()

for i in range(1, N):
    actual = Array[i]
    j = i - 1

    while j >= 0 and Array[j] > actual:
        Array[j + 1] = Array[j]
        j -= 1
    Array[j + 1] = actual

print("\nEl Array ordenado es: ")
for i in range(N):
    print(Array[i], end=" ")
