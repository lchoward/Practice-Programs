"""
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.
"""


class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        hashmap = {}
        # sort strings, insert into dict
        for string in strs:
            sorted_string = ''.join(sorted(string))
            if sorted_string not in hashmap:
                hashmap[sorted_string] = [string]
            else:
                hashmap[sorted_string].append(string)

        res = [val for val in hashmap.values()]
        return res


if __name__ == '__main__':
    soln = Solution()
    test_str1 = ["eat", "tea", "tan", "ate", "nat", "bat","beak"]
    test_str2 = []
    test1 = soln.groupAnagrams(test_str1)
    test2 = soln.groupAnagrams(test_str2)
    print(test1)
    print(test2)