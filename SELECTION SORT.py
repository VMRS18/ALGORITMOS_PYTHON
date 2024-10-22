# SELECTION SORT
N = int(input("Ingrese la cantidad de elementos del Array: "))
Array = []

for i in range(N):
    n = int(input(f"Ingrese el valor {i+1}: "))
    Array.append(n)

print("El Array original es: ")
for i in range(N):
    print(Array[i], end=" ")
print()

for i in range(N):
    for j in range(i + 1, N):
        if Array[i] > Array[j]:
            Array[i], Array[j] = Array[j], Array[i]

print("\nEl Array ordenado es: ")
for i in range(N):
    print(Array[i], end=" ")
