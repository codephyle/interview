# You are given a list of N points (x1, y1), (x2, y2), ..., (xN, yN) representing a polygon. You can assume these points are given in order; that is, you can construct the polygon by connecting point 1 to point 2, point 2 to point 3, and so on, finally looping around to connect point N to point 1.


# Determine if a new point p lies inside this polygon. (If p is on the boundary of the polygon, you should return False).
def is_point_inside_polygon(polygon, p):
    n = len(polygon)
    inside = False

    p1x, p1y = polygon[0]
    for i in range(n + 1):
        p2x, p2y = polygon[i % n]
        if p[1] > min(p1y, p2y):
            if p[1] <= max(p1y, p2y):
                if p[0] <= max(p1x, p2x):
                    if p1y != p2y:
                        xinters = (p[1] - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                    if p1x == p2x or p[0] <= xinters:
                        inside = not inside
        p1x, p1y = p2x, p2y

    return inside
