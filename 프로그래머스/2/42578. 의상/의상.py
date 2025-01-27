from itertools import combinations


def solution(clothes):
    answer = 0
    dic={}
    
    for i in clothes:
        if i[1] not in dic:
            dic[i[1]]=[]
        dic[i[1]].append(i[0])
    val=1
    print(dic)
    for i in dic:
        print(len(dic[i]))
        val*=len(dic[i])+1
    return val-1