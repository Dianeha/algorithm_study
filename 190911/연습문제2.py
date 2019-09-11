# 연습문제2 - 16진수 > 2진수 변환 후 앞에서부터 7bit씩 묶어 십진수 변환
hexaToBin = ['0000','0001', '0010','0011','0100','0101','0110','0111','1000','1001','1010','1011','1100','1101','1110','1111']
hexa = [str(i) for i in range(10)] + ['A', 'B', 'C', 'D', 'E', 'F']
# def hexaToBin(n):
#     Bin = ''
#
#     while (len(Bin) != 4):
#         Bin += str(n % 2)
#         n = n // 2
#
#     return Bin[::-1]


input1 = '0F97A3'
input2 = '01D06079861D79F99F'

BinNum = []
# for number in input1:
#     if number == 'A':
#         BinNum.append(hexaToBin(10))
#     elif number == 'B':
#         BinNum.append(hexaToBin(11))
#     elif number == 'C':
#         BinNum.append(hexaToBin(12))
#     elif number == 'D':
#         BinNum.append(hexaToBin(13))
#     elif number == 'E':
#         BinNum.append(hexaToBin(14))
#     elif number == 'F':
#         BinNum.append(hexaToBin(15))
#     else:
#         BinNum.append(hexaToBin(int(number)))

for number in input1:
        BinNum.append(hexaToBin[hexa.index(number)])

res = ''.join(BinNum)
print(res)

for i in range(len(res)//7):
    seven = res[7 * i : 7 * (i+1)]
    sum = 0
    for idx, digit in enumerate(seven):
        sum += int(digit) * 2**(6-idx)
    print(sum, end=' ')

sum = 0
for i in range(len(res)%7):
    sum += int(res[-(i+1)]) * 2**(i)
print(sum, end=' ')

