class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        for ghost in ghosts:
            ghosts_x,ghosts_y=ghost
            if abs(target[0]) + abs(target[1]) >= abs(ghosts_x-target[0]) + abs(ghosts_y-target[1]):
                return False
        return True
        