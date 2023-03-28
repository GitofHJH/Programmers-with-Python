# https://school.programmers.co.kr/learn/courses/30/lessons/42628
import heapq

class DualPriorityQueue:
    def __init__(self):
        self.min_heap = [] # 최소 힙
        self.max_heap = [] # 최대 힙
        
    def insert(self, num):
        heapq.heappush(self.min_heap, num)
        heapq.heappush(self.max_heap, -num)
        
    def delete_min(self):
        if not self.min_heap:
            return None
        min_num = heapq.heappop(self.min_heap)
        self.max_heap.remove(-min_num)
        return min_num
        
    def delete_max(self):
        if not self.max_heap:
            return None
        max_num = -heapq.heappop(self.max_heap)
        self.min_heap.remove(max_num)
        return max_num
    
    def isEmpty(self):
        if self.min_heap == []:
            return True
        return False

def solution(operations):
    dpq = DualPriorityQueue()
    for op in operations:
        if op == "D 1":
            dpq.delete_max()
        elif op == "D -1":
            dpq.delete_min()
        else:
            _, num = op.split()
            dpq.insert(int(num))
    
    if dpq.isEmpty():
        return [0, 0]
    max_num = dpq.delete_max()
    dpq.insert(max_num)
    min_num = dpq.delete_min()
    return [max_num, min_num]