# https://school.programmers.co.kr/learn/courses/30/lessons/150368
from itertools import product

def solution(users, emoticons):
    discount_rate = list(product([0.4, 0.3, 0.2, 0.1], repeat=len(emoticons)))
    max_plus_service = 0
    max_total_charge = 0
    for discount in discount_rate:
        plus_service = 0
        total_charge = 0
        for user_rate, user_charge in users:
            charge = 0
            user_rate /= 100
            for rate, emoticon in zip(discount, emoticons):
                if rate >= user_rate:
                    charge += emoticon * (1 - rate)
            if charge >= user_charge:
                plus_service += 1
            else:
                total_charge += charge
        if plus_service > max_plus_service:
            max_plus_service = plus_service
            max_total_charge = total_charge
        elif plus_service == max_plus_service and total_charge > max_total_charge:
            max_total_charge = total_charge
    return [max_plus_service, max_total_charge]