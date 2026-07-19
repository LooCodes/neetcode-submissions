class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        sol = defaultdict(list)
        for word in strs:
            match = [0] * 26
            for c in word:
                match[ord(c)-ord('a')] += 1
            sol[tuple(match)].append(word)
        return list(sol.values())
            
