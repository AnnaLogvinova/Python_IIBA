#Найдите произведение элементов списка с нечетными номерами.
#Найдите наибольший элемент списка, затем удалите его и выведите новый список.

import random

n = int(input("Введите размер списка n: \n"))
A = [random.randint(0, 10) for i in range(n)]
B = []
print(A)
max = A[0]
mult = 1

for i in range(len(A)):
    if i % 2 != 0:
        mult = mult * A[i]
    if A[i] > max:
        max = A[i]
i = 0
while i < len(A):
    if A[i] == max:
        del A[i]
    else:
        i += 1


print("\nПроизведение элементов списка с нечетными номерами: " + str(mult) + "\n")
print("Список А после удаления наибольшго элемента списка: " + str(A))