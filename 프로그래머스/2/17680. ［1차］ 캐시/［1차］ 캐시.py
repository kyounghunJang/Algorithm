from collections import deque

def solution(cacheSize, cities):
    answer = 0
    que=deque()
    cities=[i.upper() for i in cities]
    
    if cacheSize==0:
        return len(cities)*5
    for i in cities:
        if i not in que:
            if len(que) ==cacheSize:
                que.popleft()
            que.append(i)
            answer+=5
        else:
            que.remove(i)
            que.append(i)
            answer+=1
    return answer