import sys
input = sys.stdin.readline

n, s = map(int, input().rstrip().split(" "))

nums = list(map(int, input().rstrip().split(" ")))

i = 0
j = 0

sum_num = nums[0]
min_len = n + 1

while True:
    if sum_num >= s:
        if j - i + 1 < min_len: # 최소 길이 갱신
            min_len = j - i + 1
        
        if sum_num - nums[i] >= s:
            sum_num -= nums[i]
            i += 1
        else:
            if j + 1 <= n - 1:
                j += 1
                sum_num += nums[j]
            else:
                break
    else:
        if j + 1 <= n - 1:
            j += 1
            sum_num += nums[j]
        else:
            break

print(0 if min_len == n + 1 else min_len)