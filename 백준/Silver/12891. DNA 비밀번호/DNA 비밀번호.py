import sys
input = sys.stdin.readline

def check_valid_password(curr, password):
    for i in range(4):
        if curr[i] < password[i]:
            return False
    return True

dna_dictionary = {
    'A': 0,
    'C': 1,
    'G': 2,
    'T': 3,
}

s, p = map(int, input().rstrip().split(" "))

dna_string = input().rstrip()

password = list(map(int, input().rstrip().split(" ")))
curr = [0, 0, 0, 0]

for i in range(p):
    curr[dna_dictionary[dna_string[i]]] += 1


i = 0
j = p - 1

answer = 1 if check_valid_password(curr, password) else 0 


while (j < s - 1):
    curr[dna_dictionary[dna_string[i]]] -= 1
    i += 1
    j += 1
    curr[dna_dictionary[dna_string[j]]] += 1
    
    if check_valid_password(curr, password):
        answer += 1

print(answer)