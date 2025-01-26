from collections import deque

def solution(s):
    answer = 0
    element_que=deque(list(s))
    for _ in range(len(s)):
        stack=[]
        flag=0
        for i in element_que:
            if i=='(' or i=='{' or i=='[':
                stack.append(i)
            elif len(stack)==0:
                flag=1
                break
            if (stack[-1] == '(' and i==')') or (stack[-1] == '{' and i=='}') or (stack[-1] == '[' and i==']'):
                stack.pop()
        element_que.append(element_que.popleft())
        if flag==1 or len(stack)>0:
            continue
        else:
            answer+=1
    
    return answer