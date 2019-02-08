class Solution:
    circle_id = 0

    def next_circle_id(self):
        self.circle_id += 1
        return self.circle_id

    def findCircleNum(self, M):
        """
        :type M:list[list[int]]
        :rtype: int0
        """
        m_length = len(M)

        circle_map = [-1 for i in range(m_length)]  # type: list[list[int]]

        def merge(x, y):
            x_circle = circle_map[x]
            y_circle = circle_map[y]

            if x_circle != -1 and y_circle != -1 and x_circle == y_circle:
                return

            if x_circle == -1 and y_circle != -1:
                circle_map[x] = circle_map[y]
            elif x_circle != -1 and y_circle == -1:
                circle_map[y] = circle_map[x]
            elif x_circle == -1 and y_circle == -1:
                new_circle_id = self.next_circle_id()
                circle_map[x] = new_circle_id
                circle_map[y] = new_circle_id
            else:
                new_circle_id = self.next_circle_id()
                circle_map[x] = new_circle_id
                circle_map[y] = new_circle_id
                for index in range(len(circle_map)):
                    circle = circle_map[index]
                    if circle == x_circle or circle == y_circle:
                        circle_map[index] = new_circle_id

        for i in range(m_length):
            has_friend = False
            for j in range(m_length):
                if M[i][j]:
                    merge(i, j)
                    has_friend = True
            if not has_friend:
                circle_map[i] = self.next_circle_id()

        return len(set(circle_map))


if __name__ == '__main__':
    solution = Solution()
    print(solution.findCircleNum([[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
