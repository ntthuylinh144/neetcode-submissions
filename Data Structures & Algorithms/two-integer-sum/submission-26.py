class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index_i = 0
        index_s = 0
        for i in nums:
            if i == target/2 and i in nums[nums.index(i)+1:]:
                index_i = nums.index(i)
                nums.remove(i)
                index_s = nums.index(i)+1
                return [index_i, index_s]
            s = target - i
            
            if s in nums[nums.index(i)+1:]: 
                index_i = nums.index(i)
                index_s = nums.index(s) 
                return [index_i, index_s]