class Vertex:

    def __init__(self, key):
        self.id = key
        self.color = None
        self.depth = None
        self.precursor = None
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

    def BFS(self, startVertex):
        WHITE = 0
        GRAY = 1
        BLACK = 2
        MAX = 1000000000000000
        for vertex in self.vertexList[startVertex].keys():
            vertex.color = WHITE
            vertex.depth = MAX
            vertex.precursor = None
        startVertex.color = GRAY
        startVertex.depth = 0
        startVertex.precursor = None
        queue = []
        queue.append(startVertex)
        while queue:
            u = queue[1]
            queue.remove(queue[1])
            union = []
            for i in u.connectedTo:
                if i.color == WHITE:
                    union.append(i)
            for v in union:
                if v.color == WHITE:
                    v.color = GRAY
                    v.depth = u.depth + 1
                    v.precursor = u
                    queue.append(v)
            u.color = BLACK

    def DFS(self):

        global time
        time = 0


        def DFSVISIT(self, vertex):
            time += 1
            vertex.d = time
            vertex.color = GRAY
            for v in self.vertexList[vertex].keys():
                if v.color == WHITE:
                    v.precursor = vertex
                    DFSVISIT(v)
            vertex.color = BLACK
            time += 1
            vertex.f = time


        WHITE = 0
        GRAY = 1
        BLACK = 2
        MAX = 1000000000000000
        for vertex in self.vertexList:
            vertex.color = WHITE
            vertex.precursor = None
        for vertex in self.vertexList:
            if vertex.color == WHITE:
                DFSVISIT(vertex)
