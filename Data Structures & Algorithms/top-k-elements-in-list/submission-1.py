class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        n = Counter(nums)
        top_k = n.most_common(k)
        return [x for (x,y) in top_k]