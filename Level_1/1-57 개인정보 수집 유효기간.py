def cal(day, period):
    year, month, date = day.split('.')
    year = int(year)
    month = int(month) + period

    while month > 12:
        month -= 12
        year += 1
    return str(year) + '.' + str(month).zfill(2) + '.' + date

def solution(today, terms, privacies):
    term_dic = {}
    for term in terms:
        x, y = term.split()
        term_dic[x] = int(y)
    
    results = []
    for privacy in privacies:
        day, term = privacy.split()
        results.append(cal(day, term_dic[term]))
    
    answer = []
    for i, result in enumerate(results):
        if result <= today:
            answer.append(i+1)
    return answer