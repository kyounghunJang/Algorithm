def solution(bandage, health, attacks):
    answer = health
    curr=0
    prev=0
    heal_hp=0
    for curr,j in attacks:
        time=curr-prev-1
        if time >= bandage[0]:
            heal_hp+=bandage[2]*(time//bandage[0])
        heal_hp+=time*bandage[1]
        answer+=heal_hp
        heal_hp=0
        if answer > health:
            answer=health
        answer-=j
        if answer <= 0:
            return -1
        prev=curr
    if answer <=0:
        return -1
    return answer