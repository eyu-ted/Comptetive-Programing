class Solution:
    def maximumEnergy(self, energy: List[int], k: int) -> int:
        maxx = float("-inf")
        for i in range(len(energy)-1,-1,-1):
            if i  +k <len(energy):
                energy[i] += energy[i+k]
            maxx = max(maxx,energy[i])
        
        return maxx
        