class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        l1=[]
        for i,num1 in enumerate(nums):
            for j,num2 in enumerate(nums):
                if i==j:
                    pass
                else:
                    if target==num1 + num2:
                        l1.append(i)
        return l1
