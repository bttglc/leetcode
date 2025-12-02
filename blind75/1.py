class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        partial = {}
        for i in range(0, len(nums)):
            current_number = nums[i]
            complement = target - current_number
            if complement in partial:
                return [partial[complement], i]
            else:
                partial[current_number] = i
