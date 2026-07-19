class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        import heapq 
        cnter = Counter(nums)
        ans = []
        for (num, freq) in cnter.items():
            ans.append((-freq,num))
        heapq.heapify(ans)

        sol = []
        for i in range(k):
            sol.append(heapq.heappop(ans)[1])
        return sol
