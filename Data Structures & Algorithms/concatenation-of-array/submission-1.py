class Solution:
    def getConcatenation(self, nums):

        n = len(nums)
        ans = [0] * (2 * n)

        for i in range(n):
            ans[i] = ans[i+n] = nums[i]
        
        return ans

if __name__ == "__main__":
    nums = [1, 4, 6]

    result = Solution().getConcatenation(nums)
    if result:
        print(result)  

