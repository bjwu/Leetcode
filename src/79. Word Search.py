class Solution:
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        def dfs(board, word, t, path):
            x, y = t[0], t[1]
            if len(word) == 0:
                return True
            else:
                done1 =  done2 = done3 = done4 = False
                if x > 0 and board[x-1][y] == word[0]:
                    if (x-1,y) not in path:
                        path[(x-1,y)] = 1
                        done1 = dfs(board, word[1:], (x-1,y), path)
                if y > 0 and board[x][y-1] == word[0]:
                    if (x, y-1) not in path:
                        path[(x,y-1)] = 1
                        done2 = dfs(board, word[1:], (x,y-1), path)
                if x < m and board[x+1][y] == word[0]:
                    if (x+1, y) not in path:
                        path[(x+1,y)] = 1
                        done3 = dfs(board, word[1:], (x+1,y), path)
                if y < n and board[x][y+1] == word[0]:
                    if (x, y+1) not in path:
                        path[(x,y+1)] = 1
                        done4 =  dfs(board, word[1:], (x,y+1), path)
                if done1 or done2 or done3 or done4:
                    return True
                else:
                    del path[t]
                    return False

        m, n = len(board)-1, len(board[0])-1
        if len(word) == 0:
            return False
        for i in range(m+1):
            for j in range(n+1):
                if board[i][j] != word[0]:
                    continue
                else:
                    if dfs(board, word[1:], (i,j), {(i,j):1}):
                        return True
        return False