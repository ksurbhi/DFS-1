from queue import Queue
###################### Method 1: BFS ######################
class Solution:
    """
    Time Complexity: O(m*n)
    Space Complexity: O(m*n)
    m: No of rows in the matrix
    n: No of Columns in the matrix
    """
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        # Initialize queues for rows and columns
        rowQ = Queue()
        colQ = Queue()
        
        # Store the original color of the starting pixel
        oldColor = image[sr][sc]
        
        # If the color to fill is the same as the original color, no need to proceed
        if oldColor == color:
            return image
        
        # Enqueue the starting pixel's row and column
        rowQ.put(sr)
        colQ.put(sc)
        
        # Define the four possible directions to move in the matrix (Up, Down, Left, Right)
        Dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        
        # While there are still pixels to process in the queue
        while not rowQ.empty():
            # Dequeue the current pixel's row and column
            r = rowQ.get()
            c = colQ.get()
            
            # Set the current pixel to the new color
            image[r][c] = color
            
            # Check all four directions
            for d in Dirs:
                nr = r + d[0]  # New row index
                nc = c + d[1]  # New column index
                
                # If the new position is within bounds and matches the old color, enqueue it
                if 0 <= nr < len(image) and 0 <= nc < len(image[0]) and image[nr][nc] == oldColor:
                    rowQ.put(nr)
                    colQ.put(nc)
        
        # Return the modified image
        return image


############################ Method 2: DFS ##################     
class Solution:
   """
    Time Complexity: O(m*n)
    Space Complexity: O(m*n)
    m: No of rows in the matrix
    n: No of Columns in the matrix
    """
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image == None or len(image) == 0 or image[sr][sc] == color:
            return image
        
        # Define the four possible directions to move in the matrix (Up, Down, Left, Right)
        self.Dirs = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        self.oldColor = image[sr][sc]
        self.dfs(image,sr,sc,color)
        return image
    
    def dfs(self, image: List[List[int]], row: int, col: int, color: int):
        if row <0 or row == len(image) or col <0 or col == len(image[0]) or image[row][col] != self.oldColor:
            return
        #logic
        image[row][col] = color
        for d in self.Dirs:
            nr = row+d[0]
            nc = col+d[1]
            self.dfs(image,nr,nc,color)


        
