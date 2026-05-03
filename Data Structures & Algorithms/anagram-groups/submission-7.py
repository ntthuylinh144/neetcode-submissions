class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for s in strs:
            key = ''.join(sorted(s))  # O(k log k)
            groups[key].append(s)

        return list(groups.values())