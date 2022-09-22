from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i
        return

# Example 1:
nums1 = [2,7,11,15]
target1 = 9
#---> Output: [0,1]

# Example 2:
nums2 = [3,2,4]
target2 = 6
#---> Output: [1,2]

# Example 3:
nums3 = [3,3]
target3 = 6
#---> Output: [0,1]

if __name__== "__main__":
    s = Solution()
    print("Output 1: ", s.twoSum(nums1, target1))
    print("Output 2: ", s.twoSum(nums2, target2))
    print("Output 3: ", s.twoSum(nums3, target3))