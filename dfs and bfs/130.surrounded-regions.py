#
# @lc app=leetcode id=130 lang=python3
#
# [130] Surrounded Regions
#

# @lc code=start



class UnionFind:
    def __init__(self, n):
        self.count = n
        self.parents = list(range(n))
        self.sizes = [1]*n
    
    def find(self, x):
        while self.parents[x] != x:
            # path compression
            self.parents[x] = self.parents[self.parents[x]]
            x = self.parents[x]
        return x
    
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        
        if root_x == root_y:
            return
        
        if (self.sizes[root_x] > self.sizes[root_y]):
            self.parents[root_y] = root_x
            self.sizes[root_x] += self.sizes[root_y]
        else:
            self.parents[root_x] = root_y
            self.sizes[root_y] += self.sizes[root_x]
        self.count -= 1
    
    def is_connected(self, x, y):
        return self.find(x) == self.find(y)


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:
            return
        # Union Find
        num_rows = len(board)
        num_cols = len(board[0])
        # (i, j) cell map to i*num_cols + j
        uf = UnionFind(num_rows*num_cols+1)
        # num_rows*num_cols is dummy that represents border
        border = num_rows*num_cols

        # connect O on the board with the border dummy
        for i in (0, num_rows-1):
            for j in range(num_cols):
                if board[i][j] == 'O':
                    uf.union(i*num_cols+j, border)
        for i in range(num_rows):
            for j in (0, num_cols-1):
                if board[i][j] == 'O':
                    uf.union(i*num_cols+j, border)

        # work interior of the board
        for i in range(1, num_rows-1):
            for j in range(1, num_cols-1):
                if board[i][j] == 'O':
                    for m, n in ((i-1, j), (i+1, j), (i, j-1), (i, j+1)):
                        if board[m][n] == 'O':
                            uf.union(i*num_cols+j, m*num_cols+n)
        
        for i in range(num_rows):
            for j in range(num_cols):
                if board[i][j] == 'O' and not uf.is_connected(i*num_cols+j, border):
                    board[i][j] = 'X'



        
        # # BFS accepted
        # from collections import deque
        # if not board:
        #     return
        
        # num_rows = len(board)
        # num_cols = len(board[0])

        # q = deque()
        # # put all O on the board in the queue
        # for i in (0, num_rows-1):
        #     for j in range(num_cols):
        #         if board[i][j] == 'O':
        #             q.append((i, j))
        # for i in range(num_rows):
        #     for j in (0, num_cols-1):
        #         if board[i][j] == 'O':
        #             q.append((i, j))
        
        # while q:
        #     i, j = q.popleft()
        #     if (0 <= i < num_rows) and (0 <= j <num_cols):
        #         board[i][j] = '.'
        #         for m, n in ((i-1, j), (i+1, j), (i, j-1), (i, j+1)):
        #             if (0 <= m < num_rows) and (0 <= n <num_cols) and board[m][n] == 'O':
        #                 q.append((m, n))
        
        # for i in range(num_rows):
        #     for j in range(num_cols):
        #         if board[i][j] == '.':
        #             board[i][j] = 'O'
        #         elif board[i][j] == 'O':
        #             board[i][j] = 'X'
        
        # # too slow
        # # bfs and color
        # if not board:
        #     return

        # not_surrounded = set()
        # num_rows = len(board)
        # num_cols = len(board[0])

        # border = [(0, i) for i in range(num_cols)]
        # border.extend(((num_rows-1, i) for i in range(num_cols)))
        # border.extend(((i, 0) for i in range(num_rows)))
        # border.extend(((i, num_cols-1) for i in range(num_rows)))

        # q = deque()

        # def validate(i, j):
        #     return (0 <= i < num_rows) and (0 <= j <num_cols)
        
        # def get_adjacencies(i, j):
        #     return ((i-1, j), (i+1, j), (i, j-1), (i, j+1))

        # for i, j in border:
        #     # print(i, j)
        #     if board[i][j] == 'O' and (i, j) not in not_surrounded:
        #         q.append((i, j))
        #         while q:
        #             # print(q)
        #             cell = q.popleft()
        #             not_surrounded.add(cell)
        #             for m, n in get_adjacencies(*cell):
        #                 # print('adj: ', m, n)
        #                 if validate(m, n) and board[m][n] == 'O' and (m, n) not in not_surrounded:
        #                     q.append((m, n))

        # for i in range(num_rows):
        #     for j in range(num_cols):
        #         if (i, j) not in not_surrounded:
        #             board[i][j] = 'X'        

        # # Too Slow

        # if not board:
        #     return

        # visited_O = set()
        # num_rows = len(board)
        # num_cols = len(board[0])

        # def validate(i, j):
        #     return (0<= i < num_rows) and (0<= j <num_cols)
        
        # def get_adjacencies(i, j):
        #     return ((i-1, j), (i+1, j), (i, j-1), (i, j+1))

        # def is_on_border(i, j):
        #     return i == 0 or i == num_rows-1 or j == 0 or j == num_cols-1           

        # q = deque()
        # possible_flips = set()

        # for i in range(num_rows):
        #     for j in range(num_cols):
        #         if board[i][j] == 'O' and (i, j) not in visited_O:
        #             q.append((i, j))
        #             surrounded = True
                    
        #             while q:
        #                 cell = q.popleft()
        #                 possible_flips.add(cell)
        #                 if is_on_border(*cell):
        #                     surrounded = False
        #                 for m, n in get_adjacencies(*cell):
        #                     if validate(m, n) and board[m][n] == 'O' and (m, n) not in possible_flips:
        #                         q.append((m, n))
                    
        #             if surrounded:
        #                 for m, n in possible_flips:
        #                     board[m][n] = 'X'
        #             else:
        #                 visited_O.update(possible_flips)
                    
        #             possible_flips.clear()
# @lc code=end

