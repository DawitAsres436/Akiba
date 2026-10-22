class Solution:
    def missingNumber(self, nums: list[int]) -> int:
        number = set(nums)
        for i in range(len(number)+1):
            if i not in number:
                return i

        