"""This is going to be a rewritten, improved, and simplified version of the
Pythonds library that the textbook uses."""

class Graph:
    def __init__(self):
        """create an empty dictionary that will hold 'point:[(x,y), (x1,y1)]'
        where point is any given node, and the listed objects are the points it
        connects to"""
        self.vertices = {}
        self.connectedTo = {}
    
    def addVertex(self, point):
        """called after checking that a vertex is not already in the dictionary
        and creates a new entry with the origin point key and empty list"""
        self.connectedTo[point] = []
        
    def addEdge(self, origin, end):
        #check that the points are not already in the dictionary
        if origin not in self.vertices:
            self.addVertex(origin)
        self.connectedTo[origin].append(end)
    
    def getConnections(self):
        return self.connectedTo.keys()
    
    def setColor(self, color):
        self.color = color

    def getColor(self):
        return self.color