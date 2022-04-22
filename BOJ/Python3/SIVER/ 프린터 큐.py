# 백준 온라인 저지 1966번
import sys
from collections import deque

n, m = map(int, input().split()) # N <- 문서의 개수 / M <- 궁금한 문서의 인덱스 번호
imp = deque(map(int, input().split())) # 문서들의 중요도

if 