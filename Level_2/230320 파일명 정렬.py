def sort(data):
    x = data[0].lower()
    y = int(data[1])
    return x, y

def solution(files):
    for i, file in enumerate (files):
        temp = []
        file += ' '
        flag = False
        for idx, s in enumerate(file):
            if not flag and s.isdigit():
                flag = True
                # head
                temp.append(file[:idx])
                digit_start = idx
            elif flag and not s.isdigit():
                # number
                temp.append(file[digit_start:idx])
                # tail
                temp.append(file[idx:-1])
                break
        files[i] = temp
    print(files)
    files = sorted(files, key=sort)
    return [''.join(x) for x in files]

a = ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"]
b = ['F-15']
print(solution(b))