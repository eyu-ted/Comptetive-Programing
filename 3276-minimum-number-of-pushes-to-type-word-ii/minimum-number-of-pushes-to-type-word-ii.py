class Solution:
    def minimumPushes(self, word: str) -> int:
        dic = Counter(word)
        def my(ch):
            return dic[ch]
        lis = []
        for ch in word:
            lis.append(ch)

        lis.sort(key= my,reverse = True)

        c =0
        ans =0
        check = set()
        for ch in lis:
            if ch not in check:
                ans += (dic[ch]*((c//8)+1))
                check.add(ch)
                c+=1
        return ans
        

        