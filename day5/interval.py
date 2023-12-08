# Python Code for Interval tree
class Interval:
    def __init__(self, low, high):
        if(low>high):
            raise Exception('bad interval')
        self.low = low
        self.high = high
 
    def __str__(self):
        return "[" + str(self.low) + "," + str(self.high) + "]"

class IntervalDist:
    def __init__(self, low, high,dstDist):
        if(low>high):
            raise Exception('bad interval')
        self.low = low
        self.high = high
        self.dstDist = dstDist
 
    def __str__(self):
        return "[" + str(self.low) + "," + str(self.high) + "]"
 
 
class Node:
    def __init__(self, range, max,dstDist):
        self.range = range
        self.max = max
        self.left = None
        self.right = None
        self.dstDist = dstDist
 
    def __str__(self):
        return "[" + str(self.range.low) + ", " + str(self.range.high) + "] " + "max = " + str(self.max) + ", src to dest= "+ str(self.dstDist) + "\n"
 
 
def insert(root, x,dstDist):
    if root == None:
        return Node(x, x.high,dstDist)
 
    if x.low < root.range.low:
        root.left = insert(root.left, x,dstDist)
    else:
        root.right = insert(root.right, x,dstDist)
 
    if root.max < x.high:
        root.max = x.high
 
    return root
 
 
def inOrder(root):
    if root == None:
        return
 
    inOrder(root.left)
    print(root, end="")
    inOrder(root.right)
 
 
def isOverlapping(root, x):
    if root == None:
        # return a dummy interval range
        return Interval(-1, -1)
 
    # if x overlaps with root's interval
    if (x.low > root.range.low and x.low < root.range.high or (x.high > root.range.low and x.high < root.range.high)):
        return root.range
 
    elif (root.left != None and root.left.max > x.low):
        # the overlapping node may be present in left child
        return isOverlapping(root.left, x)
 
    else:
        return isOverlapping(root.right, x)

def srcIntervalToDstInterval(root, x):
    #no overlap
    if root == None:
        return [x]
 
    # complete overlap
    if (x.low >= root.range.low and x.low <= root.range.high and x.high >= root.range.low and x.high <= root.range.high):
        return [Interval(x.low+root.dstDist,x.high+root.dstDist)]
    
    #Partial overlap low side
    if (x.low >= root.range.low and x.low <= root.range.high):
        return [Interval(x.low+root.dstDist,root.range.high+root.dstDist)] + srcIntervalToDstInterval(root,Interval(root.range.high+1,x.high))

    #Partial overlap high side
    if (x.high >= root.range.low and x.high <= root.range.high):
        return [Interval(root.range.low+root.dstDist,x.high+root.dstDist)] + srcIntervalToDstInterval(root,Interval(x.low,root.range.low-1))
 
    elif (root.left != None and root.left.max >= x.low):
        # the overlapping node may be present in left child
        return srcIntervalToDstInterval(root.left, x)
 
    else:
        return srcIntervalToDstInterval(root.right, x)

def srcToDest(root, x):
    if root == None:
        # return a dummy interval range
        return x
 
    # if x overlaps with root's interval
    if (x >= root.range.low and x <= root.range.high):
        return x + root.dstDist
 
    elif (root.left != None and root.left.max >= x):
        # the overlapping node may be present in left child
        return srcToDest(root.left, x)
 
    else:
        return srcToDest(root.right, x)

def srcToDstList(src,lst):
    for i in lst:
        #full overlap
        if (src.low >= i.low and src.low <= i.high and src.high >= i.low and src.high <= i.high):
            return [Interval(src.low+i.dstDist,src.high+i.dstDist)]
        
        #partial overlap low side
        if(src.low >= i.low and src.low <= i.high):
            return [Interval(src.low+i.dstDist,i.high+i.dstDist)] + srcToDstList(Interval(i.high+1,src.high),lst)

        #partial overlap high side
        if(src.high >= i.low and src.high <= i.high):
            return [Interval(i.low+i.dstDist,src.high+i.dstDist)] + srcToDstList(Interval(src.low,i.low-1),lst)

    return [src]
 
 
if __name__ == '__main__':
    root = None
    root = insert(None, Interval(15, 20),2)
    root = insert(root, Interval(10, 30),2)
    root = insert(root, Interval(17, 19),2)
    root = insert(root, Interval(6, 20),2)
    root = insert(root, Interval(12, 15),2)
    root = insert(root, Interval(30, 40),2)
 
    print("Inorder traversal of constructed Interval Tree is")
    inOrder(root)
    print()
    i = Interval(6, 6)
    print("Searching for interval", i)
    print("Overlaps with ", isOverlapping(root, i))
 
# This code is contributed by Tapesh (tapeshdua420)
