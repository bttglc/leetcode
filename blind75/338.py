class Solution:
    max = 100_000
    dp = [0] * max
        
    # populate
    dp = [bin(i).count(1) for i in range(0, max)]

    def countBits(self, n: int) -> List[int]:
        ans = self.dp[:n+1]
        return ans
        
