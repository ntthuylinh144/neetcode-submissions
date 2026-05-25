class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        r = []
        for i in range(len(nums)):
            n_left = nums[:i:1]
            n_right = nums[i+1::1]
            r.append(math.prod(n_left)*math.prod(n_right))
        return r