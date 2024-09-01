class Solution:
    def is_anagram(self, s: str, t: str) -> bool:
        for i in max(s, t):
            if s.count(i) != t.count(i):
                return False

        return True


solution = Solution()
print(solution.is_anagram("rat", "car"))
