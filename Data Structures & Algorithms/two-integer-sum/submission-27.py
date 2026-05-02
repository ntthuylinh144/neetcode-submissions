class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in nums:
            index_i = nums.index(i)
            s = target - i

            if s in nums[index_i + 1:]:
                index_s = nums.index(s, index_i + 1)
                return [index_i, index_s]

        return []