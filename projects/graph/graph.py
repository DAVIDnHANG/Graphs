"""
Simple graph implementation
"""
from util import Queue, Stack  # These may come in handy

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
        self.vertices[v1].add(v2)

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
        check = set() # Keep track of already used vertices
        FIFOque = Queue() # Make a Queue
        FIFOque.enqueue(starting_vertex)
        check.add(starting_vertex)
        while FIFOque.size() > 0:
            node_index = FIFOque.dequeue() # Get current node
            print(node_index)
            for edge in self.vertices[node_index]:  # Go through all unused neighbors
                if edge not in check:
                    FIFOque.enqueue(edge) # Enqueue vertex
                    check.add(edge)

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
            print(LookAtThisNode)
            for oneEdge in self.vertices[LookAtThisNode]:
                if oneEdge not in upkeep:
                    FirstInLastOut.push(oneEdge)
                    upkeep.add(oneEdge)
    def dft_recursive(self, starting_vertex, UntilStackIsEmpty=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        #start with a node, and EmptyStack
        if UntilStackIsEmpty == None:
            UntilStackIsEmpty = set()
            UntilStackIsEmpty.add(starting_vertex)
        lookAtThisNode = self.vertices[starting_vertex]
        print(starting_vertex)
        for edges in lookAtThisNode:
            if edges not in UntilStackIsEmpty:
                UntilStackIsEmpty.add(edges)
                self.dft_recursive(edges,UntilStackIsEmpty)

    def bfs(self, starting_vertex, destination_vertex ):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # make a Check to not duplicate serached, and FIFO queue, put in starting_vertex into both
        check = set()
        FIFO = Queue()
        FIFO.enqueue((starting_vertex, []))
        check.add(starting_vertex)
        #start with a vertex's index, create a pathing, then start pushing edges into the FIFO queue.
        #return when vertexIndex == destination_vertex
        while FIFO.size()>0:
            ThisVertex=FIFO.dequeue()
            VertexIndex = ThisVertex[0]
            VertexPathing = ThisVertex[1].copy() # return the pathing variable
            VertexPathing.append(VertexIndex) # append to pathing variable
            if VertexIndex == destination_vertex:
                return VertexPathing
            for edge in self.vertices[VertexIndex]:
                if edge not in check:
                    FIFO.enqueue((edge, VertexPathing))
                    check.add((edge))
        return None


    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        #
        upkeep = set() # Keep track of already used vertices with list of path travelled
        FIFOStack = Stack() # Make a Stack
        FIFOStack.push((starting_vertex, [])) # Push starting vertex
        upkeep.add(starting_vertex)
        while FIFOStack.size() > 0:
            Vertex = FIFOStack.pop() # Get current node
            Vertex_index = Vertex[0]
            pathing = Vertex[1].copy()
            pathing.append(Vertex_index) # Add current vertex to path
            if Vertex_index == destination_vertex: # Return if at destination
                return pathing
            for edge in self.vertices[Vertex_index]:  # Go through all unused neighbors
                if edge not in upkeep:
                    FIFOStack.push((edge, pathing)) # Push vertex with list of path travelled
                    upkeep.add(edge)
        return None

    def dfs_recursive(self, starting_vertex, destination_vertex, startingPath=[], check=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        #create VectexPath,
        if check == None: # Make new used set if not one (initial call)
            check = set()
            check.add(starting_vertex)
        Vertex_path = startingPath.copy()
        Vertex_path.append(starting_vertex) # Add current vertex to path
        if starting_vertex == destination_vertex: # Return if starting=destination
            return Vertex_path
        for edge in self.vertices[starting_vertex]:  # Go thought one of the edge
            if edge not in check:
                check.add(edge)
                node_path = self.dfs_recursive(edge, destination_vertex, node_path, check) # Pass through used set
                if node_path[-1] == destination_vertex: # Return list if found the solution
                    return node_path
        return startingPath # Default returning original list

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
