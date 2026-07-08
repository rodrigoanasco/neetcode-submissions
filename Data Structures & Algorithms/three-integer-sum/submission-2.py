class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        answer = []
        nums.sort()
        print(nums)
        for i in range(len(nums) - 2):
            a = nums[i]
            b = i + 1
            c = len(nums) - 1

            print("current number (a):", a, "|| index:", i, "iterating")
            temp = []
            while(b < c):
                if nums[b] + nums[c] + a > 0:
                    print("current number (c):", nums[c], "|| index:", c, "decreasing")
                    c -= 1
                elif a + nums[b] + nums[c] < 0:
                    print("current number (b):", nums[b], "|| index:", b, "increasing")
                    b += 1
                    nums[b]
                elif a + nums[b] + nums[c] == 0:
                  temp.append(a)
                  temp.append(nums[b])
                  temp.append(nums[c])
                  if temp not in answer:
                    answer.append(temp)
                  temp = []
                  b += 1
                  c -= 1

        
        print(answer)
        return answer
                