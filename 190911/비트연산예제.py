def Bbit_print(i):
    output = ""
    for j in range(7, -1, -1):
        output += "1" if i & (1 << j) else "0"
    print(output)



# 비트연산 예제3

n = 0x00111111
# n    : 00000000 00010001 00010001 00010001
#        0x00        1   1    1   1    1   1
# 0xff : 00000000 00000000 00000000 11111111
if n & 0xff:
    print("Little endian")
else:
    print("big endian")

# 비트연산 예제5
a = 0x86
key = 0xAA

print('a     ==>', end=' ')
Bbit_print(a)

print('a^=key==>', end=' ')
a ^= key
Bbit_print(a)

print('a^=key==>', end=' ')
a ^= key
Bbit_print(a)



