class Solution:
    #def twoSum(self, nums, target):
    #    """
    #    :type nums: List[int]
    #    :type target: int
    #    :rtype: List[int]
    #    """
    #    diction={}
    #    for i in range(len(nums)):
    #        print (diction)
    #        if diction.get(nums[i]) is not None:
    #            return [diction.get(nums[i]), i]
    #        else:
    #            diction[target - nums[i]] = i
    def twoSum(self,nums,target):
        for i in range(len(nums)):
            e1=nums.pop(0)
            print (nums)
            if (target-e1 in nums):
                return [i,i+nums.index(target-e1)+1]

x=Solution()
nums=[3,4,6,7,8,3]
target=14
print(x.twoSum(nums,target))
