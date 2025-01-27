# def solution(citations):
#     answer = 0
#     citations.sort()
#     length= len(citations)

#     for i in range(length):
#         if length-i >= citations[i] and i<=citations[i]:
#             answer=citations[i]
#         else:
#             break
#             return answer

#     return answer
def solution(citations):
    citations.sort()  # 논문의 인용 횟수를 오름차순 정렬
    length = len(citations)

    for i in range(length):
        h = length - i  # h 이상 인용된 논문의 수
        if h <= citations[i]:  # h 조건 만족
            return h  # 가장 큰 h 반환
    
    return 0  # 조건 만족하지 않는 경우
