from collections import deque
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        # Missed the edge case.
        if not board or not board[0]:
            return
        
        # Initialize the matrix with 1.
        # Then do graph traversal on the edges if you find 'O' initialize it with 1 and 
        # rest of the connected components with same 0.
        
        row, column = len(board), len(board[0])
        # Not correct way of initializing.
        # visited = [[0]*column]*row
        visited = [[0 for _ in range(column)] for _ in range(row)]
        #print(visited)
        
        for i in range(row):
            
            if board[i][0] == 'O':
                #traverse
                self.bfs(board, visited, (i, 0), row, column)
            if board[i][column - 1] == 'O':
                #traverse
                self.bfs(board, visited, (i, column-1), row, column)
        for i in range(column):
            
            if board[0][i] == 'O':
                #traverse
                self.bfs(board, visited, (0, i), row, column)
            if board[row - 1][i] == 'O':
                #traverse
                self.bfs(board, visited, (row-1,i), row, column)
                
        # Updating the matrix
        for i in range(row):
            for j in range(column):
                if board[i][j] == 'O' and visited[i][j] == 0:
                    board[i][j] = 'X'
      
    def bfs(self, board, visited, start, row, column):
        
        # write a bfs.
        
        # create a queue and add the start position.
        # Insert childrens and update the visited matrix and return.
        directions = [(1,0), (0,1), (0,-1), (-1,0)]
        queue = deque()
        queue.append(start)
        visited[start[0]][start[1]] = 1
        while queue:
            x, y = queue.popleft()
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < row and 0 <= ny < column and board[nx][ny] == 'O' and visited[nx][ny] == 0:
                    queue.append((nx, ny))
                    visited[nx][ny] = 1
                    
                
            
        
        
    
    
        
