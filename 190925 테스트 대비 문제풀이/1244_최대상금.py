import sys
sys.stdin = open('input1244.txt', 'r')


###### 32888 케이스 미통과 >> 같은 큰 수가 있으면 뒤의 것과 바꿈 -- 수정필요
for tc in range(1, int(input())+1):
    nums, cnt = input().split()
    nums = [int(x) for x in nums]
    cnt = int(cnt)
    compareNums = sorted(nums, reverse=True)
    i = 0
    while cnt:
        if nums == compareNums:
            for k in range(len(nums)-1):
                if nums[k] == nums[k+1]:
                    flag = False
                    break
            while cnt: # 같은 수가 없으면 k가 len(nums)-2에 도달해서 cnt가 0이 될 때까지 마지막 두개를 바꾸게 됨
                nums[k], nums[k+1] = nums[k+1], nums[k]
                cnt -= 1
            break

        temp = []
        unordered = nums[i+1::]
        m = max(unordered)
        for j in range(len(unordered)):
            if unordered[j] == m:
                temp.append(j+i+1)
        if nums[i] <= nums[temp[-1]]:
            nums[i], nums[temp[-1]] = nums[temp[-1]], nums[i]
            cnt -= 1
            i += 1
        else:
            i += 1
    print('#%d' % tc, ''.join(map(str, nums)))
