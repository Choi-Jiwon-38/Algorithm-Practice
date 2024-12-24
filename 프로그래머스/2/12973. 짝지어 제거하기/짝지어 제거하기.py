def solution(s):
    a = ["" for _ in range(len(s) + 1)]

    # '커서'라고 지칭
    idx = 0
    for c in s:
        if a[idx] == '':    # 현재 커서에 비어있는 경우
            a[idx] = c      # 다음에 올 값을 채워준다
        elif (s[idx] == c): # 현재 커서와 다음에 올 값이 같은 경우
            a[idx] = ''     # 지움 처리
            idx -= 1
        elif (s[idx] != c): # 현재 커서와 다음에 올 값이 다른 경우
            idx += 1        
            a[idx] = c      # 다음 칸에 채움 처리
            
    # 전체를 짝지어 제거할 수 있는 문자열이었다면 a[idx]가 ''일 것
    return 1 if a[idx] == '' else 0