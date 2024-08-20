from typing import List
from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # hashmap = {}
        # result = []
        # for num in nums:
        #     hashmap[num] = hashmap.get(num, 0) + 1
        # hashmap = {key: val for key, val in sorted(hashmap.items(), key=lambda item: -item[1])}
        # for val in hashmap:
        #     if (k == 0): break
        #     result.append(val)
        #     k -= 1
        # return result
        counter = Counter(nums)
        return [item for item, _ in counter.most_common(k)]


def main():
    nums = [1, 2, 2, 3, 3, 3, 3]
    k = 2
    print(Solution().topKFrequent(nums, k))

if __name__ == "__main__":
    main()