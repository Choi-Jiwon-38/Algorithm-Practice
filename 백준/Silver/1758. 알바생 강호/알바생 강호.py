import sys
input = sys.stdin.readline

n = int(input())
tips = []

for _ in range(n):
    tips.append(int(input()))

tips.sort(reverse=True)

answer = 0
order = 1

for tip in tips:
    answer += max(0, tip - (order - 1))
    order += 1

print(answer)