from collections import deque

def solution(order):
    new_order = [0] * len(order)
    for idx, od in enumerate(order):
        new_order[od-1] = idx+1
    main_q = deque(new_order)
    sub_q = deque()   
    
    result = 0
    target = 1
    
    while True:
        if (not main_q) and (not sub_q):
            break
            
        if (not main_q) and (sub_q[-1] != target):
            break

        if main_q and main_q[0] == target:
            main_q.popleft()
            target += 1
            result += 1
            continue
        
        elif sub_q and sub_q[-1] == target:
            sub_q.pop()
            target += 1
            result += 1
            continue
        else:
            sub_q.append(main_q.popleft())            
    
    return result