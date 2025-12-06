import sys
from collections import deque
input = sys.stdin.readline


n = int(input())
word = input().rstrip()

convert_map = dict()
curr_alphabet_ascii_code = 65

for i in range(n):
    convert_map[chr(curr_alphabet_ascii_code)] = input().rstrip()
    curr_alphabet_ascii_code += 1

# number string을 저장하는 용도(피연산자들 저장)
stack = deque([])

# 후위 표기식을 deque 형태로 변환하여 할당
word_deque = deque(list(word))


# char가 영대문자(A~Z)에 해당하는지 검증하는 함수
def isAlphabet(char):
    ascii_num = ord(char)
    return True if ascii_num >= 65 and ascii_num <= 90 else False


while len(word_deque) > 0:
    curr_char = word_deque.popleft()

    if isAlphabet(curr_char): # curr_char가 영대문자(A~Z)인 경우
        stack.append(convert_map[curr_char]) # `convert_map`을 통하여 영대문자를 number string으로 변환한 뒤, stack에 저장
    else: # curr_char가 피연산자인 경우

        # 연산을 위해 stack에 저장된 number string 2개를 pop
        y = str(stack.pop())
        x = str(stack.pop())

        # `eval()`를 통해 연산된 결과를 다시 stack에 append
        stack.append(eval(x + curr_char + y))


# 소숫점 계산 둘쨰 자리까지만 노출
# 1. f-string을 이용해서 f"{number:.2f}"
# 2. round를 이용해서 round(number, 2)
#    (주의점) 3번째 자리에서 반올림을 진행하므로 문제 요구 사항 정확히 파악 필요 
print(f"{float(stack[0]):.2f}")
