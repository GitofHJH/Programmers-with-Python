def solution(dartResult):
    a = ''
    b = ''
    c = ''
    ans1=''
    ans2=''
    ans3=''
    alcnt = 0
    for dart in dartResult:
        if dart.isalnum():
            if alcnt == 0:
                if dart.isdigit():
                    a += dart
                elif dart.isalpha():
                    a += dart
                    alcnt += 1
            elif alcnt == 1:
                if dart.isdigit():
                    b += dart
                elif dart.isalpha():
                    b += dart
                    alcnt += 1
            else:
                if dart.isdigit():
                    c += dart
                elif dart.isalpha():
                    c += dart
                    alcnt += 1
        else:
            if alcnt == 1:
                a += dart
            elif alcnt == 2:
                b += dart
            else:
                c += dart

    for i in a:
        if i.isdigit():
            ans1 = ans1+i
        elif i.isalpha():
            ans1 = int(ans1)
            if i == 'S':
                ans1 = ans1**1
            elif i == 'D':
                ans1 = ans1**2
            else:
                ans1 = ans1**3
        else:
            if i == '*':
                ans1 = ans1*2
            else:
                ans1 = ans1*(-1)

    for i in b:
        if i.isdigit():
            ans2 = ans2+i
        elif i.isalpha():
            ans2 = int(ans2)
            if i == 'S':
                ans2 = ans2**1
            elif i == 'D':
                ans2 = ans2**2
            else:
                ans2 = ans2**3
        else:
            if i == '*':
                ans2 = ans2*2
                ans1 = ans1*2
            else:
                ans2 = ans2*(-1)

    for i in c:
        if i.isdigit():
            ans3 = ans3+i
        elif i.isalpha():
            ans3 = int(ans3)
            if i == 'S':
                ans3 = ans3**1
            elif i == 'D':
                ans3 = ans3**2
            else:
                ans3 = ans3**3
        else:
            if i == '*':
                ans3 = ans3*2
                ans2 = ans2*2
            else:
                ans3 = ans3*(-1)

    return sum([ans1,ans2,ans3])