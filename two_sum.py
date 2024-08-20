from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            val = target - nums[i]
            if val in hashmap:
                return [hashmap[val], i]
            hashmap[nums[i]] = i
        return []


def main():
    nums = [i for i in range(10000000)]    
    target = 178321
    print(Solution().twoSum(nums, target))

if __name__ == "__main__":
    main()