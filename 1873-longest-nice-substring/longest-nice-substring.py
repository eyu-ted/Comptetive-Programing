class Solution:
  def longestNiceSubstring(self, s: str) -> str:
    if len(s) < 2:
      return ''

    sett = set(s)

    for i, c in enumerate(s):

      if c.swapcase() not in sett:
        prefix = self.longestNiceSubstring(s[:i])
        suffix = self.longestNiceSubstring(s[i + 1:])
        return max(prefix, suffix, key=len)

    return s