def solution(clothes):
    answer = 1
    closet = {}
    for c in clothes:
        if not c[1] in closet.keys():
            closet[c[1]] = []
        closet[c[1]] += [c[0]]
    print(closet)
    for (key, val) in closet.items():
        answer *= len(val) + 1

    return answer - 1

clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]
solution(clothes)