n,m= map(int, input().split())

data=[]

def sol(start):
    if len(data)==m:
        print(" ".join(map(str,data)))
        return
    else:
        for i in range(start,n+1):
            data.append(i)
            sol(i)
            data.pop()

sol(1)
