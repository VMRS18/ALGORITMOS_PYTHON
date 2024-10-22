# BURBBLE SORT
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
    for j in range(N-1):  # Ajuste para evitar desbordamiento de índice
        if Array[j] > Array[j+1]:
            Array[j], Array[j+1] = Array[j+1], Array[j]  # Swap en Python

print("\nEl Array ordenado es: ")
for i in range(N):
    print(Array[i], end=" ")
