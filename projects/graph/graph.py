"""
Simple graph implementation
"""
import dll_queue, dll_stack  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertiecs[v1].add(v2)
        else:
            print("ERROR: Vertex,", v1, ",is not found")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        #use python dictionary at vertex_id, then add the edge to neightbors.
        neightbors=set() #same as {}
        for edge in self.vertices[vertex_id]:
            neightbors.add(edge)
        return neightbors

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        #Start a que FIFO,
        #use the queue stack to make while loop.
        #dequeue FIFO, then look at all its edges.
        #put those edges into the FIFO queue.
        #then look at the FIFO's edges
        InQueue = set()#
        FirstInFirstOut = Queue()#
        FirstInFirstOut.enqueue(starting_vertex)
        InQueue.add(starting_vertex)
        while FirstInFirstOut.size() >0:
            currentFIFO = FirstInFirstOut.dequeue()
            currentVertices = self.vertices(currentFIFO)
            for FIFOsEdges in currentVertices:
                if FIFOsEdges not in InQueue: #maybe i can use queue directly?
                    FirstInFirstOut.enqueue(FIFOsEdges)
                    InQueue.add(FIFOsEdges)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        #push starting_vertex into stack.
        #look at ONE edge from starting_vertex.
        #push that one edge into stack, then look at its edge.
        #continue this pattern, avoid looking up edges that are connected.
        upkeep = set()
        FirstInLastOut = Stack()
        FirstInLastOut.push(starting_vertex)
        upkeep.add(starting_vertex)
        while FirstInLastOut.size() > 0:
            LookAtThisNode = FirstInLastOut.pop()
            workingOnThisVertex = self.vertices[LookAtThisNode]
            for oneEdge in workingOnThisVertex:
                if oneEdge not in upkeep:
                    FirstInLastOut(oneEdge)
                    upkeep.add(oneEdge)
    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        pass  # TODO

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        pass  # TODO

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        pass  # TODO

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        pass  # TODO

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
