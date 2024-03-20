n = int(input())
pos = list(map(int, input().split()))
speed= list(map(int, input().split()))

def checker(t):

    minn = float("-inf")
    maxx = float("inf")
    for i in range(len(pos)):
        a= pos[i]-(t*speed[i])
        b=pos[i]+(t*speed[i])
        if b<minn:
            return False
        if a>maxx:
            return False
            
        if a>minn:
            minn=a
        if b<maxx:
            maxx=b

   
    return True




l=0
r= 1e9

while r-l>10e-8:

    midd = (r+l)/2

    if checker(midd):
        r=midd
    else:
        l=midd
        
print(l)