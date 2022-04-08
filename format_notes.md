Triangular coordinates are (x,y) coordinates starting from the top left giving the triangles filling in a hexagon. In a hexagon of size n, there are a total of 4n-1 rows, n in increasing size from 2 to 2n, 2n-1 rows of 2n and then n rows of decreasing size from 2n to 2.

A move is a pairs:
* List[int]: a position in triangular coordinates, giving the top left of the hexagon
* Bool: True if "pulling", False if "Pulling"

A configuration is a 2d array of integers (in triangular coordinates) 0:6 where the number represents the direction of connection, starting at horizontal right and moving counterclockwise.
