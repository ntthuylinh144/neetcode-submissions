class Solution:
    def createDict(self, s:str):
        dict_s = {}
        for i in s:
            dict_s[i] = dict_s.get(i, 0) + 1
        return dict_s 

    def is2Anagrams(self, a: str, b:str) -> bool:
        if len(a) != len(b): return False
        dict_a = self.createDict(a)
        dict_b = self.createDict(b)
        if dict_a != dict_b: return False
        return True

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        results = []
        groups = {}
        for s in strs: #grouping 
            if len(s) in groups.keys():
                groups[len(s)].append({s: False})
            else:
                groups[len(s)] = [{s: False}]
        
        for k, v  in groups.items():
            for i, item in enumerate(v):
                for k1, v1 in item.items():
                    if k==1 and len(v)==1:
                        results.append([k1])
                    else:
                        for i, item in enumerate(v):
                            for k1, v1 in item.items():
                                if v1== False:
                                    r = [k1]
                                    item[k1] = True
                                    for j in range(i+1, len(v)):
                                        item1 = v[j]
                                        for k2, v2 in item1.items():
                                            if v2 == False and self.is2Anagrams(k1, k2) == True:
                                                r.append(k2)
                                                item1[k2] = True
                                    results.append(r)
        return results