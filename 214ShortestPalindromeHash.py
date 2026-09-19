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
    def shortestPalindrome(self, s: str) -> str:
        prefix = 0
        suffix = 0
        base = 29
        last_index = 0
        mod = 10**9 + 7

        for i, c in enumerate(s):
            prefix = (prefix * base + ord(c)) % mod
            suffix = (suffix + pow(base, i, mod) * ord(c)) % mod

            if prefix == suffix:
                last_index = i

        suffix = s[last_index + 1:][::-1]
        return suffix + s

if __name__ == "__main__":
    solver = Solution()

    # "aacecaaa"
    print(solver.shortestPalindrome("aacecaaa"))
    # "abcd"
    print(solver.shortestPalindrome("abcd"))