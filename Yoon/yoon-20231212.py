class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        # for i in range(len(nums)-1):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]

        # n² => Refactoring(Use Dictionary)
        num_dict = {}

        for idx in range(len(nums)):
            num = nums[idx]
            sub_value = target - num

            if sub_value in num_dict:
                return [num_dict[sub_value], idx]

            num_dict[num] = idx
