class Vertex:

    def __init__(self, key):
        self.id = key
        self.connectedTo = []

    def addNeiborVertex(self, neiborVertex, weight=None):
        self.connectedTo[neiborVertex] = weight

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self, neiboVertex):
        return self.connectedTo[neiboVertex]

class Graph:

    def __init__(self):
        self.vertexList = {}
        self.numOfVertex = 0

    def addVertex(self, key):
        self.numOfVertex += 1
        newVertex = Vertex(key)
        self.vertexList[key] = newVertex
        return newVertex

    def getVertex(self, n):
        if n in self.vertexList:
            return self.vertexList[n]
        else:
            return None

    def addEdge(self, f, t, cost=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], cost)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())
