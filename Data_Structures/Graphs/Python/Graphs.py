"""
Graph Implementation

This module provides a Graph data structure implementation using an adjacency list.
The implementation supports directed/undirected graphs and weighted/unweighted graphs.
"""

class Graph:
    """
    Graph implementation using an adjacency list.
    
    This implementation can represent both directed and undirected graphs.
    Vertices can be of any hashable type (strings, numbers, etc.).
    
    Attributes:
        adjacency (dict): Dictionary mapping vertices to their adjacent vertices.
        directed (bool): Flag indicating if the graph is directed.
    """
    
    def __init__(self, directed=False):
        """
        Initialize an empty Graph.
        
        Args:
            directed (bool): True: the graph is directed; False: the graph is undirected.
        """
        self.adjacency = {}
        self.directed = directed

    def add_vertex(self, v):
        """
        Add a vertex to the graph if it doesn't already exist.
        
        Args:
            v: The vertex to add (can be any hashable type).
        """
        if v not in self.adjacency:
            self.adjacency[v] = []

    def add_edge(self, v1, v2, weight=None):
        """
        Add an edge between vertices v1 and v2.
        
        If the vertices don't exist, they will be added to the graph.
        For undirected graphs, edges are added in both directions.
        
        Args:
            v1: The first vertex.
            v2: The second vertex.
            weight: Optional weight for the edge.
        """
        if v1 not in self.adjacency:
            self.add_vertex(v1)
        if v2 not in self.adjacency:
            self.add_vertex(v2)

        # For weighted graphs, store (vertex, weight) tuples
        if weight is not None:
            # Check if edge already exists
            for i, (vertex, _) in enumerate(self.adjacency[v1]):
                if vertex == v2:
                    # Update weight if edge exists
                    self.adjacency[v1][i] = (v2, weight)
                    if not self.directed:
                        for i, (vertex, _) in enumerate(self.adjacency[v2]):
                            if vertex == v1:
                                self.adjacency[v2][i] = (v1, weight)
                    return
            
            # Add new edge with weight
            self.adjacency[v1].append((v2, weight))
            if not self.directed:
                self.adjacency[v2].append((v1, weight))
        else:
            # For unweighted graphs, just store the vertex
            if v2 not in self.adjacency[v1]:
                self.adjacency[v1].append(v2)
                if not self.directed:
                    self.adjacency[v2].append(v1)

    def get_neighbors(self, v):
        """
        Get all vertices adjacent to vertex v.
        
        Args:
            v: The vertex to get neighbors for.
            
        Returns:
            list: A list of adjacent vertices. If the vertex doesn't exist, returns an empty list.
        """
        return self.adjacency.get(v, [])
    
    def remove_edge(self, v1, v2):
        """
        Remove the edge between vertices v1 and v2.
        
        Args:
            v1: first vertex.
            v2: second vertex.
            
        Returns:
            bool: True if the edge was removed, False if it didn't exist.
        """
        if v1 in self.adjacency and v2 in self.adjacency:
            # Handle weighted edges
            if self.adjacency[v1] and isinstance(self.adjacency[v1][0], tuple):
                for i, (vertex, _) in enumerate(self.adjacency[v1]):
                    if vertex == v2:
                        self.adjacency[v1].pop(i)
                        if not self.directed:
                            for i, (vertex, _) in enumerate(self.adjacency[v2]):
                                if vertex == v1:
                                    self.adjacency[v2].pop(i)
                        return True
            # Handle unweighted edges
            else:
                if v2 in self.adjacency[v1]:
                    self.adjacency[v1].remove(v2)
                    if not self.directed:
                        self.adjacency[v2].remove(v1)
                    return True
        return False
    
    def remove_vertex(self, v):
        """
        Remove a vertex and all its edges from the graph.
        
        Args:
            v: The vertex to remove.
            
        Returns:
            bool: True if the vertex was removed, False if it didn't exist.
        """
        if v in self.adjacency:
            # Remove the vertex from the adjacency list
            del self.adjacency[v]
            
            # Remove any edges pointing to this vertex
            for vertex in self.adjacency:
                # Handle weighted edges
                if self.adjacency[vertex] and isinstance(self.adjacency[vertex][0], tuple):
                    self.adjacency[vertex] = [(u, w) for u, w in self.adjacency[vertex] if u != v]
                # Handle unweighted edges
                else:
                    if v in self.adjacency[vertex]:
                        self.adjacency[vertex].remove(v)
            return True
        return False
    
    def get_vertices(self):
        """
        Get all vertices in the graph.
        
        Returns:
            list: A list of all vertices in the graph.
        """
        return list(self.adjacency.keys())
    
    def get_edges(self):
        """
        Get all edges in the graph.
        
        Returns:
            list: A list of tuples (v1, v2) or (v1, v2, weight) for all edges in the graph.
        """
        edges = []
        for v1 in self.adjacency:
            for v2 in self.adjacency[v1]:
                # Handle weighted edges
                if isinstance(v2, tuple):
                    vertex, weight = v2
                    if self.directed or (v1, vertex, weight) not in edges and (vertex, v1, weight) not in edges:
                        edges.append((v1, vertex, weight))
                # Handle unweighted edges
                else:
                    if self.directed or (v1, v2) not in edges and (v2, v1) not in edges:
                        edges.append((v1, v2))
        return edges

    def __str__(self):
        """
        Return a string representation of the graph.
        
        Returns:
            str: A string showing each vertex and its adjacent vertices.
        """
        return "\n".join([f"{v}: {neighbors}" for v, neighbors in self.adjacency.items()])


# Example usage
if __name__ == "__main__":
    # Create an undirected graph
    print("Creating an undirected graph:")
    graph = Graph()
    
    # Add vertices
    print("\nAdding vertices A, B, C, D, E")
    for vertex in ["A", "B", "C", "D", "E"]:
        graph.add_vertex(vertex)
    
    # Add edges
    print("\nAdding edges")
    graph.add_edge("A", "B")
    graph.add_edge("A", "C")
    graph.add_edge("B", "D")
    graph.add_edge("C", "D")
    graph.add_edge("D", "E")
    
    # Print the graph
    print("\nGraph structure:")
    print(graph)
    
    # Get neighbors
    print("\nNeighbors of vertex D:")
    print(graph.get_neighbors("D"))
    
    # Create a directed graph
    print("\n\nCreating a directed graph:")
    digraph = Graph(directed=True)
    
    # Add vertices and edges
    digraph.add_edge(1, 2)
    digraph.add_edge(1, 3)
    digraph.add_edge(2, 4)
    digraph.add_edge(3, 2)
    
    # Print the directed graph
    print("\nDirected graph structure:")
    print(digraph)
    
    # Create a weighted graph
    print("\n\nCreating a weighted graph:")
    weighted_graph = Graph()
    
    # Add weighted edges
    weighted_graph.add_edge("A", "B", 5)
    weighted_graph.add_edge("A", "C", 3)
    weighted_graph.add_edge("B", "C", 2)
    weighted_graph.add_edge("B", "D", 6)
    weighted_graph.add_edge("C", "D", 7)
    
    # Print the weighted graph
    print("\nWeighted graph structure:")
    print(weighted_graph)
    
    # Get all edges
    print("\nAll edges in the weighted graph:")
    for edge in weighted_graph.get_edges():
        print(edge)
    
    # Remove an edge and a vertex
    print("\nRemoving edge (A, B) and vertex C")
    weighted_graph.remove_edge("A", "B")
    weighted_graph.remove_vertex("C")
    
    # Print the modified graph
    print("\nModified weighted graph:")
    print(weighted_graph)