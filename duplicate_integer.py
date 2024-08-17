from typing import List
import ast
import time

#i guess hashmap is the best solution in this case (although list are better for memory)

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # curr = time.time()
        hashmap = {i: 0 for i in nums}
        for num in nums:
            hashmap[num] += 1
            if hashmap[num] > 1:
                # print(f"{time.time() - curr}")
                return True
        # print(f"{time.time() - curr}")
        return False




def main():
    with open("testfile.txt", "r") as file:
        content = file.read().strip()
    arr = ast.literal_eval(content)
    print(Solution().containsDuplicate(arr))


if __name__ == "__main__":
    main()