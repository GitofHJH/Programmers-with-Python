import re
from collections import Counter

def solution(s):
    convert = 0
    eliminate_zero = 0
    while s != "1":
        eliminate_zero += Counter(s)['0']
        s = re.sub("0", "", s)
        convert += 1
        s = bin(len(s))[2:]

    return [convert, eliminate_zero]