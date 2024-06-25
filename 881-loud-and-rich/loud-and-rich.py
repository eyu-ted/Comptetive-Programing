class Solution:
  def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
    graph = [[] for _ in range(len(quiet))]

    for v, u in richer:
      graph[u].append(v)
    

    @cache
    def dfs(u):
      ans = u

      for v in graph[u]:
        res = dfs(v)
        if quiet[res] < quiet[ans]:
          ans = res

      return ans

    result = []
    for i in range(len(graph)):
      result.append(dfs(i))
    
    return result 