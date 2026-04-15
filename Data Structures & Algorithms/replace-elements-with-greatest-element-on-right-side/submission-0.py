class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        n = len(arr)
        max_far = -1

        for i in range(n-1, -1, -1):
            count = arr[i]
            arr[i] = max_far
            max_far = max(count, max_far)

        return arr

if __name__ == "__main__":

    arr = [1, 3, 5, 6]

    result = Solution().replaceElements(arr)
    print(result)
        