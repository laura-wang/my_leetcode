class Solution:
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums.sort() # sort function is in-place function, no return

        result=0
        for i in range(len(nums)):
            if i % 2 == 0:
                result=result+nums[i]
        return result




my_solution=Solution()
nums=[1,4,3,2]
print(my_solution.arrayPairSum(nums))
