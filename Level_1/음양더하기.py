def solution(absolutes, signs):
    for i in range(len(absolutes)):
        if signs[i] == 0:
            absolutes[i] = -1 * absolutes[i]

    return sum(absolutes)

