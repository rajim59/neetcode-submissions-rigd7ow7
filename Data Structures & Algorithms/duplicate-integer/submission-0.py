class Solution:
    def hasDuplicate(self, nums: list[int]) -> bool:

        seen = set()

        for i in nums:
            if i in seen:
                return True
            seen.add(i)
        
        return False

if __name__ == "__main__":
    nums = [2, 5, 8, 9]

    if Solution().hasDuplicate(nums):
        print("Yes")

    else:
        print("No")



