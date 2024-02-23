t=int(input())
for _ in range(t):
    n=int(input())
    s=input()
    dic={0:1}
    ans=0
    tot=0
    for i in range(n) :
        tot+=int(s[i])
        diff=tot-(i+1)
        ans+=dic.get(diff,0)
        dic[diff]=1+dic.get(diff,0)
          
        
        
    print(ans)