from Point import Point
from functools import reduce

'''
Code Cited
--------------------------------
Algorithm for Graham Scan
http://tomswitzer.net/2010/03/graham-scan/
https://www.ics.uci.edu/~eppstein/161/python/diameter.py
Algorithm for Jarvis March
https://gist.github.com/tixxit/252222

'''
def graham_scan(pts): # O(n log n)
    ''' Computes the upper and lower hulls for a given set of points and chains them together for a covex hull '''
    u = []
    l = []
    pts = sorted(pts) #O(n log n) time to sort
    for pt in pts:
        # Remove all collinear and clockwise turns from upper hull
        while len(u) > 1 and pt.orientation(u[-2], u[-1]) <= 0:
            u.pop()
        # Remove all collinear and counter clockwise turns lower hull
        while len(l) > 1 and pt.orientation(l[-2], l[-1]) >= 0:
            l.pop()
        u.append(pt)
        l.append(pt)
    # Concat the upper and lower hulls in order
    return u+[l[i] for i in range(len(l)- 2, 0, -1)]

def _next_hull_pt(pt, pts):
    q = pt
    for r in pts:
        orientation = pt.orientation(q, r)
        if (orientation < 0 or orientation == 0 and pt.dist(r) > pt.dist(q)):
            q = r
    return q 

def jarvis_march(pts): # O(nh) n = # pts, h = # of pts on hull
    ''' Algorithm to compute the Convex Hull by computing on point on the hull at a time '''
    hull = [min(pts)] # Get the far left point, O(n)
    for pt in hull:
        q = _next_hull_pt(pt, pts)
        if q != hull[0]:
            hull.append(q)
    return hull

