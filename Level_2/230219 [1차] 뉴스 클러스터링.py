
def solution(str1, str2):
    str1 = str1.lower()
    str2 = str2.lower()
    a = []
    b = []
    for i in range(len(str1)-1):
        if str1[i:i+2].isalpha():
            a.append(str1[i:i+2])

    for i in range(len(str2)-1):
        if str2[i:i+2].isalpha():
            b.append(str2[i:i+2])
   
    a_temp = list(a)
    union = list(a)
    for i in b:
        if i not in a_temp:
            union.append(i)
        else:
            a_temp.remove(i)

    inter = []
    for i in b:
        if i in a:
            a.remove(i)
            inter.append(i)

    if len(inter) == 0 and len(union) == 0:
        return 65536
    return int((len(inter)/len(union)) * 65536)

a = "aa1+aa2"
b = "AAAA12"
print(solution(a, b))