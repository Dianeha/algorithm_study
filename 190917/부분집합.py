# 부분집합
arr = [3,6,7,1,5,4]
n = len(arr)
cnt = 0
for i in range(0, (1<<n)): # 1을 n 만큼 shift >> 2**6승만큼 for루프가 돈다 000000 000001 000010 000011 000100 ...
    for j in range(0, n):
        if i & (1<<j):
            print(arr[j], end=' ')
    cnt+=1
    print()
    # print('>>>>>>>>>>>>>>> cnt = ', cnt)
print('==================================================')

# 조합
an = [1,2,3,4,5]
def comb(n, r):
    if r == 0:
        print(tr)
    elif n < r:
        return
    else:
        tr[r-1] = an[n-1]
        comb(n-1, r-1)
        comb(n-1, r)

tr = [0]*3
comb(5, 3)

print('==================================================')

# 연습문제3 (93p) - 바이너리 카운팅, 조합으로 풀기

arr = [-1, 3, -9, 6, 7, -6, 1, 5, 4, -2]
# n = len(arr)
# temp = []
# for i in range(0, (1<<n)):
#     temp = []
#     for j in range(0, n):
#         if i & (1<<j):
#             temp.append(arr[j])
#     if sum(temp) == 0:
#         print(temp , end=' ')

def comb2(n, r):
    if r == 0:
        if sum(tr) == 0:
            print(tr)
    elif n < r:
        return
    else:
        tr[r-1] = arr[n-1]
        comb2(n-1, r-1)
        comb2(n-1, r)

for i in range(len(arr)+1):
    tr = [0]*i
    comb2(len(arr), i)