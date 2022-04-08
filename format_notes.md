Since a lozenge tiling can be represented as a grid of heights weakly increasing in one direction, we will represent a tiling as a 2D array of numbers increasing in the negative x and y direction (so that 0,0,0 is the middle).

A move is a position as well as a "push" or a "pull" (a boolean where True is push). This position is a line coming towards the viewer and so will be represented as a 3d point on that line where one of the three coordinates is zero and the other two are positive. The total number of such coordinates is (3 * n^2) - (3*n) + 1.

Coordinates are (x, y, z) where z is vertical for 3d or (x, y) for 2d.
