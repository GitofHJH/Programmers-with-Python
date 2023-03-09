from collections import deque

def solution(cacheSize, cities):
    if cacheSize == 0:
        return len(cities) * 5
    else:
        answer = 0
        q = deque()
        for city in cities:
            city = city.lower()
            # 캐시에 참조된 도시이면 캐시 갱신
            if city in q:
                answer += 1
                q.remove(city)
                q.append(city)
            # 캐시에 참조되지 않았었고
            else:
                # 자리가 남으면
                if len(q) < cacheSize:
                    q.append(city)
                    answer += 5
                # 자리가 안남으면 
                else:
                    q.popleft()
                    q.append(city)
                    answer += 5
        return answer

cacheSize = 2
cities = ["Jeju", "Pangyo", "NewYork", "newyork"]
print(solution(cacheSize, cities))