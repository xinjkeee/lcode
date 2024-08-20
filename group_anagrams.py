from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        test = defaultdict(list)
        for word in strs:
            key = tuple(sorted(word))
            test[key].append(word)

        return list(test.values())

def main():
    strs = ["eat","tea","tan","ate","nat","bat"]
    print(Solution().groupAnagrams(strs))

if __name__ == "__main__":
    main()