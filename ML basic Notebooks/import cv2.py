t=int(input())
for i in range(t):
    a,b,c = map(int,input().split())
    if c<b & c>=a :
        print("YES")
    else:
        print("NO")