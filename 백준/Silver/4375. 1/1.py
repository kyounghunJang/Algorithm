


while True:
    try:
        n=int(input())
        num=1
    except:
        break
    while True:
        if num%n ==0 :
            print(len(list(str(num))))
            break
        num=num*10+1
