# HEAP SORT
N = int(input("Ingrese la cantidad de elementos del Array: "))
Array = []

for i in range(N):
    n = int(input(f"Ingrese el valor {i+1}: "))
    Array.append(n)

print("El Array original es: ")
for i in range(N):
    print(Array[i], end=" ")
print()

# Función para hacer heapify
def heapify(Array, N, i):
    padre = i
    hizq = 2 * i + 1
    hder = 2 * i + 2

    if hizq < N and Array[hizq] > Array[padre]:
        padre = hizq
    if hder < N and Array[hder] > Array[padre]:
        padre = hder

    if padre != i:
        Array[i], Array[padre] = Array[padre], Array[i]
        heapify(Array, N, padre)

# Construir el heap
for i in range(N // 2 - 1, -1, -1):
    heapify(Array, N, i)

# Extraer elementos del heap
for i in range(N - 1, 0, -1):
    Array[0], Array[i] = Array[i], Array[0]
    heapify(Array, i, 0)

print("\nEl Array ordenado es: ")
for i in range(N):
    print(Array[i], end=" ")
