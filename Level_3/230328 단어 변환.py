# https://school.programmers.co.kr/learn/courses/30/lessons/43163
import sys
sys.setrecursionlimit(10**6)
ans = 100

def check(a, b):
    result = 0
    for i in range(len(a)):
        if a[i] != b[i]:
            result += 1
    if result == 1:
        return True
    return False

def search(begin, target, words, visited, cnt):
    global ans
    if begin == target:
        ans = min(ans, cnt)
        return
    stack = []
    for idx, word in enumerate(words):
        if check(begin, word) and visited[idx] == False:
            visited[idx] = True
            stack.append(idx)
    while stack:
        search(words[stack.pop()], target, words, visited, cnt + 1)

def solution(begin, target, words):
    global ans
    if target not in words:
        return 0
    visited = [False] * len(words)
    search(begin, target, words, visited, 0)
        
    return ans

a = 'hit'
b = 'cog'
c = ["hot", "dot", "dog", "lot", "log", "cog"]
print(solution(a,b,c))