import math

N=int(input())
A= [True]*(2000000)

for i in range(2, int(math.sqrt(len(A))+1)):
    if A[i] == False:
        continue
    for j in range(2*i, len(A),i):    
        A[j]=False
def cal(n):
    data= list(str(n))
    for i in range(0,len(data)//2):
        s=data[i]
        e=data[len(data)-i-1]
        if s!=e:
            return False
    return True        

while True:
    if N==1:
        print(2)
        break
    if A[N] ==True:
        if cal(N)==True:
            print(N)
            break
    N+=1

