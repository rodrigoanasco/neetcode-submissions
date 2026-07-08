class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        reps = {}
        answer = []

        for n in nums:
            if n not in reps:
                reps[n] = 1
            else:
                reps[n] += 1
        
        for _ in range(k):
            key_of_max = max(reps, key=reps.get)
            answer.append(key_of_max)
            reps.pop(key_of_max, None)
        
        return answer