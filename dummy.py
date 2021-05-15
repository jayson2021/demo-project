class Graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = []
            gdict = {}
        self.gdict = gdict
        self.gdict = gdict

    def getVertices(self):
        return list(self.gdict.keys())

    def countVertices(self):
        return len(list(self.gdict.keys()))

    def addVertex(self, i):
        if i not in self.gdict:
            self.gdict[i] = []

    def addEdge(self, edge):
        edge = set(edge)
        (i1, i2) = tuple(edge)
        if i1 in self.gdict:
            self.gdict[i1].append(i2)
        else:
            self.gdict[i1] = [i2]

    def findEdges(self):
        edgeName = []
        for i in self.gdict:
            for v in self.gdict[i]:
                if {v, i} not in edgeName:
                    edgeName.append({i, v})
        return edgeName

    def countEdges(self):
        return len(self.findEdges())


graph1 = {1: [2, 3, 6],
          2: [1, 3, 4],
          3: [1, 2, 4, 6],
          4: [2, 3, 5],
          5: [4, 6],
          6: [1, 3, 5]
          }

g = Graph(graph1)

print("a.", graph1)
print("b.", g.getVertices())
print("c.", g.countVertices())
print("d.", g.findEdges())
print("e.", g.countEdges())

g.addVertex(7)
g.addVertex(8)

g.addEdge({5, 3})
g.addEdge({5, 7})
g.addEdge({8, 2})
g.addEdge({8, 7})

print("\na.", graph1)
print("b.", g.getVertices())
print("c.", g.countVertices())
print("d.", g.findEdges())
print("e.", g.countEdges())

print("HELLO WORLD")
print("HELLO WORLD")
print("HELLO WORLD")
print("HELLO WORLD")
print("HELLO WORLD")

print("ABC 123")
print("ABC 123")
print("ABC 123")
print("ABC 123")
print("ABC 123")

