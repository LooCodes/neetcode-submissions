class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        sol = 1
        for num in nums: 
            sol *= num
        output = [0] * len(nums)
        for i in range(len(nums)):
            if nums[i] != 0:
                output[i] = sol // nums[i]
            else:
                # Special case for zero to avoid DivisionByZero
                p = 1
                for j, val in enumerate(nums):
                    if i != j: p *= val
                output[i] = p
        return output