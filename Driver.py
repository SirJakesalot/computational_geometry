import matplotlib.pyplot as plt
from Point import Point
from ConvexHull import ConvexHull

# Declare test case
#test_case = [(6,7), (1,9), (9,4), (1,1), (7,7), (4,1), (8,6), (8,3), (4,5), (5,4), (4,9), (6,5), (4,10), (5,8), (3,2), (1,3), (4,4), (2,5), (1,9), (5,5)]

# Convert test case into List of Point objects
def getPointsFromTuples(pts):
    pointList = []
    for pt in pts:
        pointList.append(Point(pt[0], pt[1]))
    return pointList
# Get a list of Random Point
def getRandomPoints(numOfPoints):
    pointList = []
    for pt in range(0, numOfPoints):
        pointList.append(Point())
    return pointList

# Set up matplotlib to print the points and lines
def plotLines(hull, pts):
    plt.plot([pt.x() for pt in pts], [pt.y() for pt in pts], 'ro', marker='o')
    for i in range(0,len(hull)-1):
        plt.plot([hull[i].x(), hull[i+1].x()], [hull[i].y(), hull[i+1].y()])
    plt.plot([hull[len(hull)-1].x(), hull[0].x()], [hull[len(hull)-1].y(), hull[0].y()])
    plt.axis([-11, 11, -11, 11])

# Single case
#pts = getPointsFromTuples(test_case)

for i in range(0,10):
    print("iteration", i)
    pts = getRandomPoints(20)
    # Compute the hull and print their points
    g_scan = ConvexHull(pts).graham_scan()
    j_march = ConvexHull(pts).jarvis_march()

    print("Given Points:", str(sorted(pts)))
    print("Graham_Scan:", g_scan)
    print("Jarvis_March:", j_march)
    plt.figure(1)
    plt.subplot(211)
    plotLines(g_scan, pts)
    plt.subplot(212)
    plotLines(j_march, pts)
    #plt.show()
    plt.savefig('myfig')
    break
