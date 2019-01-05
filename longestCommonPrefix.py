# https://leetcode-cn.com/explore/interview/card/bytedance/242/string/1014/
class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: list[str]
        :rtype: str
        """
        rows = len(strs)
        if rows == 0:
            return ""
        index = 0
        while index < len(strs[0]):
            c = strs[0][index]
            for s in strs:
                if index >= len(s) or s[index] != c:
                    return strs[0][0: index]
            index += 1
        return strs[0][0: index]


if __name__ == '__main__':
    solution = Solution()
    print(solution.longestCommonPrefix(["ab","abcccc"]))
