class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
         sortedNums = sorted(nums)
         dic = {}
         res = []
         for i in range(len(sortedNums)):
            if sortedNums[i] not in dic:
                dic[sortedNums[i]] = i
         for i in nums:
            res.append(dic[i])
         return res   
