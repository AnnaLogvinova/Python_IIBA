#Введите одномерный целочисленный список. Найдите наибольший нечетный элемент.
#Найдите минимальный по модулю элемент списка.
import random

n = int(input("Введите размер списка n: \n"))
A = [random.randint(-99, 99) for i in range(n)]
print(A)
max = A[0]
min = abs(A[0])

for i in range(len(A)):
    if A[i] > max and A[i] % 2 != 0:
        max = A[i]
    if abs(A[i]) < min:
        min = abs(A[i])

print("\nНаибольший нечетный элемент в списке: " + str(max) + "\n")
print("\nМинимальное по модулю элемент в списке: " + str(min) + "\n")

