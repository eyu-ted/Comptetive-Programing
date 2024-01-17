class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        prefsum=[0]*(n+1)
        for booking in bookings:
            prefsum[booking[0]-1]+=booking[2]
            prefsum[booking[1]]-=booking[2]
        for i in range(1,len(prefsum)):
            prefsum[i]+=prefsum[i-1]
        return prefsum[:n]
        
        