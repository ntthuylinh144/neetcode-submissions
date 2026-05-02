class Solution:
    def create_dict(self, s:str):
        dict_s = {}
        for i in s:
                if i not in dict_s.keys():
                    dict_s.update({f"{i}": 1})
                else:
                    dict_s.update({f"{i}": dict_s[i]+1})
        return dict_s

    def isAnagram(self, s: str, t: str) -> bool:
        len_s = len(s)
        len_t = len(t)
        if len_s != len_t: return False
        dict_s = self.create_dict(s)
        dict_t = self.create_dict(t)
        if dict_s != dict_t: return False
        return True