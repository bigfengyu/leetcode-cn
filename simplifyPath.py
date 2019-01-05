class Solution:



    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """

        def name_action(c, arr):
            if c == "/":
                return [arr, "slash"]
            else:
                name = arr.pop()
                arr.append(name + c)
                return [arr, "name"]

        def slash_action(c, arr):
            if c == "/":
                return [arr, "slash"]
            if c == ".":
                return [arr, "dot1"]
            else:
                arr.append(c)
                return [arr, "name"]

        def dot1_action(c, arr):
            if c == "/":
                return [arr, "slash"]
            if c == ".":
                return [arr, "dot2"]
            else:
                arr.append("." + c)
                return [arr, "name"]

        def dot2_action(c, arr):
            if c == "/":
                if len(arr) != 0:
                    arr.pop()
                return [arr, "slash"]
            else:
                arr.append(".." + c)
                return [arr, "name"]

        arr = []
        current_state = "name"

        action_map = {
            "name": name_action,
            "slash": slash_action,
            "dot1": dot1_action,
            "dot2": dot2_action
        }

        path = path + '/'

        for c in path:
            res = action_map[current_state](c, arr)
            arr = res[0]
            # print(current_state, '-- '+ c +' -->', end="")
            current_state = res[1]
            # print(current_state)
            # print(arr)

        return "/" + "/".join(arr)


if __name__ == '__main__':
    solution = Solution()
    print(solution.simplifyPath("///eHx/.."))
