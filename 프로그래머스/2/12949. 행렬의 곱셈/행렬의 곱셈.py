def solution(arr1, arr2):
    answer = []
    arr1_r,arr1_c= len(arr1),len(arr1[0])
    arr2_r,arr2_c=len(arr2),len(arr2[0])
    
    for i in range(arr1_r):
        line=[]
        for j in range(arr2_c):
            value=0
            for k in range(arr1_c):
                value+=arr1[i][k]*arr2[k][j]
            line.append(value)
        answer.append(line)
    
    return answer