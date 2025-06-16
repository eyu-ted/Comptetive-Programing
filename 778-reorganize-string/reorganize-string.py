class Solution:
    def reorganizeString(self, s: str) -> str:

        dic = Counter(s)
        h = []
        for ch,val in dic.items():
            h.append((val*-1, ch))
        heapify(h)

        ans = []
        q = deque()

        while h:
            cnt , ch = heappop(h)
            cnt += 1
            ans.append(ch)
            q.append((cnt,ch))
            if len(q) >= 2:
                val , ch = q.popleft()
                if val*-1:
                    heappush(h,(val, ch))
        
        return "" if len(s) != len(ans) else "".join(ans)
                
        

        