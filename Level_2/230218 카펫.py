def yaksu(n):
    n_list = []
    for i in range(1, int(n**(1/2)) + 1):
        if n % i == 0:
            n_list.append(i)
    return n_list

def solution(brown, yellow):
    for i in yaksu(yellow):
        if i + yellow // i == (brown - 4) / 2:
            return [yellow // i + 2, i + 2]

