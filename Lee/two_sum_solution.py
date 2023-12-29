class Solution(object):
    def twoSum(self, nums, target):


        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        answer_set = set()

        #for fst in nums:
        #    for sed in nums:
        #        if fst+sed == target:
        #            answer_set.add(nums.index(fst))
        #            answer_set.add(nums.index(sed))
        for fst in range(len(nums)):
            for sed in range(fst+1,len(nums)):
                if nums[fst]+nums[sed] == target:
                    return[fst,sed]