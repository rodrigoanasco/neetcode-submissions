class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        reps = {}
        temp = []

        for n in nums:
            if n not in reps:
                reps[n] = 1
            else:
                reps[n] += 1
        
        for n, c in reps.items():
            temp.append([c, n])
        temp.sort()

        answer = []
        for i in range(k):
            answer.append(temp.pop()[1])
        
        return answer