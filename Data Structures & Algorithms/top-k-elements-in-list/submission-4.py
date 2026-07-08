class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        store = defaultdict(int)        
        for i in range(len(nums)):
            store[nums[i]] += 1
        
        ans = []

        for _ in range(k):
            max_k = max(store, key=store.get)
            ans.append(max_k)
            store.pop(max_k)
        
        return ans