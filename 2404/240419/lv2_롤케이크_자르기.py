from collections import Counter
from collections import deque

def solution(topping):
    front_dict ={}
    back_dict = Counter(topping)
    front_num = 0
    back_num = len(back_dict)
    
    cnt = 0
    q = deque(topping)
    while q:
        next = q.popleft()
        if not front_dict.get(next):
            front_dict[next] = 1
            front_num += 1
            
        back_dict[next] -= 1
        if back_dict[next] == 0:
            back_num -= 1
        
        if front_num == back_num:
            cnt += 1
    
    return cnt
