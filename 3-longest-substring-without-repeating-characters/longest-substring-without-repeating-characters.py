class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        count = defaultdict(int)

        left = 0
        result = 0

        for right in range(len(s)):

            count[s[right]] += 1

            while left < right and count[s[right]] > 1:
                count[s[left]] -= 1
                left+=1

            result = max(result, right-left+1)

        return result

        