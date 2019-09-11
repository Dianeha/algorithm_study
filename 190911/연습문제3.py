hexaToBin = ['0000','0001', '0010','0011','0100','0101','0110','0111','1000','1001','1010','1011','1100','1101','1110','1111']
hexa = [str(i) for i in range(10)] + ['A', 'B', 'C', 'D', 'E', 'F']
secretPattern = ['001101', '010011','111011','110001','100011','110111','001011','111101','011001','101111']
input1 = '0DEC'
input2 = '0269FAC9A0'

BinNum = []
for number in input2:
        BinNum.append(hexaToBin[hexa.index(number)])

res = ''.join(BinNum)
print(res)

for i in range(len(res)-6):
    if res[i:i+6] in secretPattern:
        start = i
        break

for j in range(len(res)//6):
    six = res[start + 6*j:start + 6*(j+1)]
    try:
        print(secretPattern.index(six), end=' ')
    except:
        continue