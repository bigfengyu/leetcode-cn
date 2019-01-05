# https://leetcode-cn.com/explore/interview/card/bytedance/242/string/1012/
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        slength = len(s)
        if slength == 0:
            return 0

        maxlength = 1
        l = 0
        r = 1
        while r < slength:
            i = s[l:r].find(s[r]) + l
            if i >= l:
                maxlength = max(r - l, maxlength)
                l = i + 1
            r += 1
        maxlength = max(r - l, maxlength)
        return maxlength


if __name__ == '__main__':
    solution = Solution()
    print(solution.lengthOfLongestSubstring('abcabcbb'))
