input1 = '00000010001101'
input2 = '0000000111100000011000000111100110000110000111100111100111111001100111'


for i in range(len(input2)//7):
    seven = input2[7 * i : 7 * (i+1)]
    sum = 0
    for idx, digit in enumerate(seven):
        sum += int(digit) * 2**(6-idx)
    print(sum, end=' ')