import matplotlib.pyplot as plt
from Point import Point
from GeometryAlgorithms import graham_scan, jarvis_march
import time

# Declare test case
#test_case = [(6,7), (1,9), (9,4), (1,1), (7,7), (4,1), (8,6), (8,3), (4,5), (5,4), (4,9), (6,5), (4,10), (5,8), (3,2), (1,3), (4,4), (2,5), (1,9), (5,5)]

# Convert test case into List of Point objects
def getPointsFromTuples(pts):
    pointList = []
    for pt in pts:
        pointList.append(Point(pt[0], pt[1]))
    return pointList
    
# Get a list of Random Points
def getRandomPoints(numOfPoints):
    pointList = []
    s = ""
    for pt in range(0, numOfPoints):
        pointList.append(Point())
        s += str(pointList[pt]) + ", "
    return (pointList, s[:-2])
    
# Get a list of Points from a given input text
def parsePoints(input_text):
    text = input_text.replace("(", " ")
    text = text.replace(")", " ")
    text = text.replace(",", " ")
    digits = [int(x) for x in text.split()]
    return [Point(digits[i],digits[i+1]) for i in range(0,len(digits), 2)]

# Set up matplotlib to print the points and lines
def plotLines(hull, pts, rangeX, rangeY):
    plt.plot([pt.x() for pt in pts], [pt.y() for pt in pts], 'ro', marker='o')
    for i in range(0,len(hull)-1):
        plt.plot([hull[i].x(), hull[i+1].x()], [hull[i].y(), hull[i+1].y()])
    plt.plot([hull[len(hull)-1].x(), hull[0].x()], [hull[len(hull)-1].y(), hull[0].y()])
    #plt.axis([-11, 11, -11, 11])

# Single case
#pts = getPointsFromTuples(test_case)


def run(input_text = "", number_of_points = 200, rangeX = (-10,10), rangeY = (-10,10)):
    # Declare Point container
    pts = []
    # Keep string to represent the Point container, used to hash into a filename
    s = ""
    Point._rangeX = rangeX
    Point._rangeY = rangeY
    if input_text:
        pts = parsePoints(input_text)
        s = input_text
    else:
        pts,s = getRandomPoints(number_of_points)
        
    # Get unique filename to save to file system
    filepath = str(hash(s)) + '.png'
    
    # Compute the hull and print their points
    g_scan_start_time = time.time()
    g_scan = graham_scan(pts)
    g_scan_total_time = time.time() - g_scan_start_time
    
    j_march_start_time = time.time()
    j_march = jarvis_march(pts)
    j_march_total_time = time.time() - j_march_start_time
    
    # Create the figure
    fig = plt.figure(1)
    plt.axhline(0, color='white')
    plt.axvline(0, color='white')
    fig.suptitle('Convex Hull Algorithm', fontsize=14, fontweight='bold')
    
    ax1 = fig.add_subplot(211)
    ax1.set_title('Graham Scan, O(n log n), took {0} sec'.format(g_scan_total_time))

    plotLines(g_scan, pts, rangeX, rangeY)
    ax2 = fig.add_subplot(212)
    ax2.set_title('Jarvis March, O(nh), took {0} sec'.format(j_march_total_time))
    plotLines(j_march, pts, rangeX, rangeY)
    #plt.show()
    plt.savefig('/home/ubuntu/workspace/cs164/cs164/media/' + filepath)
    plt.clf()
    return '/media/' + filepath
#run2()