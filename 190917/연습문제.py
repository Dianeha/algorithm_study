# 선택정렬 함수를 재귀적 알고리즘으로 작성해보기

def SelectionSort(A):
    n = len(A)
    for i in range(0, n-1):
        min = i
        for j in range(i+1, n):
             if A[j] < A[min]:
                min = j
        A[min], A[i] = A[i], A[min]
    return A

def rec_SelectionSort(A, s, e):
    if s == e:
        return

    mini = s
    for j in range(s+1, e):
        if A[j] < A[mini]:
            mini = j

    A[s], A[mini] = A[mini], A[s]
    rec_SelectionSort(A, s+1, e)

# def SelectionSort_Recursion(A):
#     n = len(A)
#     k = 0
#     if k == n:
#         return A
#     else:
#         min = k
#         for j in range(k + 1, n):
#             if A[j] < A[min]:
#                 min = j
#         A[min], A[k] = A[k], A[min]
#         k += 1


A = [4, 52, 5, 3, 223, 67, 1, 35]
print(SelectionSort(A))
A = [4, 52, 5, 3, 223, 67, 1, 35]
# print(SelectionSort_Recursion(A))

fact = 1
for i in range(1, 7):
    fact = i * fact


print(fact)

