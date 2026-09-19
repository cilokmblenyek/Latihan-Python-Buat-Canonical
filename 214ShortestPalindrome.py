# You are given a string s. You can convert s to a palindrome by adding characters in front of it.

# Return the shortest palindrome you can find by performing this transformation.

# Example 1:

# Input: s = "aacecaaa"
# Output: "aaacecaaa"
# Example 2:

# Input: s = "abcd"
# Output: "dcbabcd"
 
# Constraints:
# 0 <= s.length <= 5 * 104
# s consists of lowercase English letters only.

class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return True
        left, right = 0, len(s) - 1
        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
        return True

    def shortestPalindrome(self, s: str) -> str:
        if not s:
            return s

        for i in reversed(range(len(s))):
            print(s[:i + 1], " ", s[i + 1:][::-1], "\n")
            if self.isPalindrome(s[:i + 1]):
                return s[i + 1:][::-1] + s
        return s

if __name__ == "__main__":
    solver = Solution()

    # "aacecaaa"
    print(solver.shortestPalindrome("aacecaaa"))
    # "abcd"
    print(solver.shortestPalindrome("abcd"))