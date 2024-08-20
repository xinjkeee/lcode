from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        mult = 1
        f = 1
        for num in nums:
            if num != 0: mult *= num
            else: f = 0
        res = [f * mult // num if num != 0 else mult for num in nums]
        return res
   

def main():
    nums = [1,2,4,6]
    print(Solution().productExceptSelf(nums))

if __name__ == "__main__":
    main()