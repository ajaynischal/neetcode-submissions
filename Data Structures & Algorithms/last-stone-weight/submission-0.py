class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #stones = [-s for s in stones]
        for i, n in enumerate(stones):
            stones[i] = -n
        heapq.heapify(stones)

        while len(stones) > 1:
            stone1 = heapq.heappop(stones)
            stone2 = heapq.heappop(stones)
            if stone2 > stone1:
                heapq.heappush(stones, stone1-stone2)
       
        stones.append(0)
        return abs(stones[0])