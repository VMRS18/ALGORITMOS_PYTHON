# QUICK SORT
N = int(input("Ingrese la cantidad de elementos del Array: "))
Array = []

for i in range(N):
    n = int(input(f"Ingrese el valor {i+1}: "))
    Array.append(n)

print("El Array original es: ")
for i in range(N):
    print(Array[i], end=" ")
print()

stack = []
top = -1

# Almacenamos el rango inicial
stack.append(0)
stack.append(N - 1)

while stack:
    alto = stack.pop()
    bajo = stack.pop()

    pivote = Array[alto]
    i = bajo - 1

    # Partimos el Array
    for j in range(bajo, alto):
        if Array[j] <= pivote:
            i += 1
            Array[i], Array[j] = Array[j], Array[i]

    Array[i + 1], Array[alto] = Array[alto], Array[i + 1]
    Lugarpivote = i + 1

    if Lugarpivote - 1 > bajo:
        stack.append(bajo)
        stack.append(Lugarpivote - 1)
    
    if Lugarpivote + 1 < alto:
        stack.append(Lugarpivote + 1)
        stack.append(alto)

print("\nEl Array ordenado es: ")
for i in range(N):
    print(Array[i], end=" ")
