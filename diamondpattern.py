n=int(input("enter: "))
a=2*n-2
for i in range(n):
    for j in range(0,a):
        print(end=' ')
    a-=1
    for j in range(0,i+1):
        print('*',end=' ')
    print('\r')
a=n-2
for i in range(n+1,-1,-1):
    for j in range(a,0,-1):
        print(end=' ')
    a+=1
    for j in range(i,0,-1):
        print('*',end=' ')
    print('\r')
