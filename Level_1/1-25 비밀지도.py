def solution(n, arr1, arr2):
    answer = []
    map1 = []
    map2 = []
    for a1 in arr1:
        b=''
        a = format(a1, 'b')
        if len(a) < n:
            a = '0'*(n-len(a)) + a
        for i in a:
            if i == '1':
                b += '#'
            else:
                b += ' '
        map1.append(b)

    for a2 in arr2:
        b=''
        a = format(a2, 'b')
        if len(a) < n:
            a = '0'*(n-len(a)) + a
        for i in a:
            if i == '1':
                b += '#'
            else:
                b += ' '
        map2.append(b)
    
    for i in range(n):
        ans = ''
        for j in range(n):
            if map1[i][j] == ' '  and map2[i][j] == ' ':
                ans += ' '
            elif map1[i][j] == '#' or map2[i][j] == '#':
                ans += '#'
        answer.append(ans)
    return answer