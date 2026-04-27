class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1

        while l < r:
            calculation = numbers[l] + numbers[r]
            if calculation < target:
                l+=1
            if calculation > target:
                r-=1

            if calculation == target:
                return [l + 1, r + 1]

        return []
            
        