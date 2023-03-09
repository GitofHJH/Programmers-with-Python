def canspeak(bab):
    speakList = ['aya', 'ye', 'woo', 'ma']
    if bab[:2] in speakList:
        present = bab[:2]
        bab = bab[2:]
        if bab == "":
            return True
        elif len(bab) < 2 or bab[:2] == present:
            return False
        else:
            canspeak(bab)
    elif bab[:3] in speakList:
        present = bab[:3]
        bab = bab[3:]
        if bab == "":
            return True
        elif len(bab) < 2 or bab[:3] == present:
            return False
        else:
            canspeak(bab)
    else:
        return False

    return canspeak(bab)

def solution(babbling):
    answer = 0
    for bab in babbling:
        if canspeak(bab) == None or canspeak(bab) == True:
            answer += 1
    return answer

babbling = ["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]
print(solution(babbling))
