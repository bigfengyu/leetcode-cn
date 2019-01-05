# https://leetcode-cn.com/explore/interview/card/bytedance/242/string/1016/
class Solution:
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        letter_dict = dict()
        s1_length = len(s1)
        for s in s1:
            if s in letter_dict:
                letter_dict[s].append(-1)
            else:
                letter_dict[s] = [-1]
        left = 0
        for index, s in enumerate(s2):
            if s in letter_dict:
                arr = letter_dict[s]  # type: list
                ix = -1

                # 存在当前串外或尚未填满可替换元素
                for j, e in enumerate(arr):
                    if e < left:
                        arr[j] = index
                        arr.sort()
                        ix = j
                        break
                # 都在串内，需要舍弃最小的
                if ix == -1:
                    left = arr[0] + 1
                    arr[0] = index
                    arr.sort()
                # print(s,arr,"s: ", s + " left: " + str(left) + " index: " + str(index))

                if index - left + 1 == s1_length:
                    # print("end s: ", s + " left: " + str(left) + " index: " + str(index))
                    return True
            else:
                left = index + 1

        return False


if __name__ == '__main__':
    solution = Solution()
    print(solution.checkInclusion("adc", "dcda"))
