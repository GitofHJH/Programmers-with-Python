def qs(array):
    if len(array) <= 1:
        return array
    pivot = array[0]
    tail = array[1:]

    left = [x for x in tail if x + pivot >= pivot + x]
    right = [x for x in tail if x + pivot < pivot + x]

    return qs(left) + [pivot] + qs(right)

def solution(numbers):
    numbers = list(map(str, numbers))
    numbers = qs(numbers)
    return ''.join(numbers)

a = [0,0,0,0]
print(set(a))
# print(solution(a))