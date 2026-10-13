class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        multiple = max(n, 2)
        
        while True:
            if multiple % 2 == 0 and multiple % n == 0:
                return multiple
                break

            multiple+=max(n, 2)