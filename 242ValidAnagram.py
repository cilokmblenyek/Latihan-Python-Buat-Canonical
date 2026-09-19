# Given two strings s and t, return true if t is an anagram of s, and false otherwise.

# Example 1:

# Input: s = "anagram", t = "nagaram"

# Output: true

# Example 2:

# Input: s = "rat", t = "car"

# Output: false

from typing import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_list = list(s)
        t_list = list(t)

        return Counter(s_list) == Counter(t_list)

if __name__ == "__main__":
    solver = Solution()
    
    # Test Case 1: s = "anagram", t = "nagaram"
    print(solver.isAnagram("anagram", "nagaram"))
    # Output: True

    # Test Case 2: s = "rat", t = "car"
    print(solver.isAnagram("rat", "car"))
    # Output: False