import sys
from tabnanny import check
input = sys.stdin.readline

#n = int(input())

check_list = []
result = []

word = "happy"
set_word = set(word)

print(word)
print(set_word)

if word[i] not in check_list:
    word