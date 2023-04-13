# https://school.programmers.co.kr/learn/courses/30/lessons/77486

def solution(enrolls, referrals, sellers, amounts):
    sales_revenue = [0 for _ in range(len(enrolls))]

    enroll_dict = {enroll:idx for idx, enroll in enumerate(enrolls)}
    referrals_dict = {enroll:referral for enroll, referral in zip(enrolls, referrals)}

    for seller, amount in zip(sellers, amounts):
        if amount == 0:
            continue
        amount *= 100
        while 1:
            rest = int(amount * 0.1)
            tmp = amount - rest
            sales_revenue[enroll_dict[seller]] = sales_revenue[enroll_dict[seller]] + tmp
            referral = referrals_dict[seller]
            if referral == "-":
                break
            seller = referral
            amount -= tmp
            if amount == 0:
                break
    return sales_revenue