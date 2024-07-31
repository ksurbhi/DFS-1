from queue import Queue

class Solution:
    """
    Without mentioning levels
    Time Complexity: O(m*n)
    Space Complexity: O(m*n)
    m: No of rows in the matrix
    n: No of Columns in the matrix
    """
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        q = Queue()
        
        # Initialize the queue with all the cells that contain 0
        # and mark cells containing 1 as -1 (unvisited).
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    q.put([i, j])  # Add position of 0s to the queue
                elif mat[i][j] == 1:
                    mat[i][j] = -1  # Mark 1s as -1 to indicate they haven't been processed yet
        
        # Define the four possible directions to move in the matrix (Up, Down, Left, Right)
        Dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        
        # BFS to update the matrix
        while not q.empty():
            r, c = q.get()  # Get the next cell from the queue
            for d in Dirs:  # Explore all four directions
                nr = r + d[0]  # Calculate new row index
                nc = c + d[1]  # Calculate new column index
                # If the new position is within bounds and hasn't been visited
                if 0 <= nr < len(mat) and 0 <= nc < len(mat[0]) and mat[nr][nc] == -1:
                    mat[nr][nc] = mat[r][c] + 1  # Update the distance from the nearest 0
                    q.put([nr, nc])  # Add the new position to the queue for further exploration
        
        return mat  # Return the updated matrix



########################### With mentioning lvls ###########################
from queue import Queue

class Solution:
"""
    With mentioning levels
    Time Complexity: O(m*n)
    Space Complexity: O(m*n)
    m: No of rows in the matrix
    n: No of Columns in the matrix
    """
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        q = Queue()  # Initialize the queue for BFS
        lvl = 0  # Initialize the level (distance from the nearest 0)
        
        # Define the possible directions (Up, Down, Left, Right)
        Dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]] 
        
        # Initialize the queue with all 0 cells and mark 1s as unvisited (-1)
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    q.put([i, j])  # Add the position of 0s to the queue
                else:
                    mat[i][j] = -1  # Mark 1s as -1 to indicate they need processing
        
        # Perform BFS
        while not q.empty():
            size = q.qsize()  # Get the number of elements at the current level
            for i in range(size):
                curr = q.get()  # Get the next cell from the queue
                for d in Dirs:  # Explore all four directions
                    nr = curr[0] + d[0]  # Calculate new row index
                    nc = curr[1] + d[1]  # Calculate new column index
                    
                    # Check if the new position is within bounds and needs processing
                    if 0 <= nr < len(mat) and 0 <= nc < len(mat[0]) and mat[nr][nc] == -1:
                        mat[nr][nc] = lvl + 1  # Update distance from the nearest 0
                        q.put([nr, nc])  # Add the new position to the queue
        
            lvl += 1  # Increment the level (distance) after processing all nodes at the current level
        
        return mat  # Return the updated matrix

