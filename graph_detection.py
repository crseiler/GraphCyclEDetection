"""Graph Class to create and identify vertices and edges.
Additional method will be to identify if a graph is cyclic"""

class Graph(object):
    def __init__(self, graph_array):
        """Initialize graph object"""
        self.__graph_array = graph_array
        
    def vertices(self):
        """returns how many vertices are in graph"""
        return
    
    def edges(self):
        """returns the edges"""
        return self.generates_edges()
    
    def generates_edges(self):
        """generates the edges of graph"""
        return
    
    def is_cyclic(self):
        return
        
        
if __name__ == "__main__":
    g = [[3],[2], [1,2,3,4], [2,3]]
    graph = Graph(g)
    print(graph.vertices())