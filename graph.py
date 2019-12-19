#Author: Akash Patel

class Graph:
    def __init__(self, graphDict):
        # Store the graph in the form of a dictionary
        self.graphDict = graphDict

    # Method to obtain the children of a vertex
    def adjacencyList(self, vertex):
        return self.graphDict.get(vertex)
