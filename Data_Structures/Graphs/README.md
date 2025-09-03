# Graphs

## Overview
A graph is a non-linear data structure consisting of nodes (**vertices**) and **edges** that connect these nodes. They are used to represent communication networks, social connections, data organization, computational devices, flow of computation, recommendation engines, etc.

## Pros
- Represents real-world relationships and connections
- Flexible structure that can model complex systems
- Supports various algorithms for path finding
- Can represent both directed and undirected relationships

## Cons
- Higher space complexity compared to linear data structures
- Operations more complex to implement
- Graph algorithms often have higher time complexity
- Visualization and traversal can be challenging

## Applications
- Social networks (connections between people)
- Web page ranking algorithms
- Mapping and navigation systems
- Network routing protocols
- Recommendation systems
- Dependency resolution in software packages

## Operations
| Operation | Time Complexity | Description |
|-----------|----------------|-------------|
| Add Vertex | O(1)           | Adding a new node to the graph |
| Add Edge   | O(1)           | Creating a connection between two nodes |
| Remove Vertex | O(V + E)    | Removing a node and all its connections |
| Remove Edge | O(E)          | Removing a connection between nodes |
| Depth-First Search | O(V + E) | Traversing the graph depth-first |
| Breadth-First Search | O(V + E) | Traversing the graph breadth-first |
| Check if edge exists | O(1) to O(V) | Checking if two nodes are connected |

## Types
Graphs come in many forms, depending on the nature of their connections:

- **Directed**: Edges have a direction, meaning the connection from node A to node B does not necessarily imply a connection from B to A (e.g., Twitter followers).
- **Undirected**: Connections are mutual, so if an edge exists from node A to node B, it also exists from B to A (e.g., Facebook friends).
- **Weighted**: Edges have a "weight" or "cost" associated with them, which can represent distance, time, or cost (e.g., a map where the weight is the distance between cities).
- **Unweighted**: The edges have no associated value; only the existence of the connection matters.
- **Cyclic**: A graph that contains at least one cycle (a path that returns to its starting node).
- **Acyclic**: A graph that contains no cycles (e.g., a tree or a Directed Acyclic Graph, or DAG).
- **Connected**: All nodes are linked in some way, so there is a path from any node to any other node.
- **Disconnected**: The graph contains isolated nodes or sub-graphs.

## Implementation Notes

In this repo, graphs are probably the most complex data structures to implement effectively. They can be stored in memory using several methods, each with its own trade-offs:

### Representation Methods

1. **Adjacency List** 
   * **Description**: The most common representation. Uses a dictionary where each key represents a node, and its value is a list of its neighboring nodes.
   * **Pros**: Space-efficient for sparse graphs (graphs with few edges). Fast to find all neighbors of a given node.
   * **Cons**: Slower to check if a direct edge exists between two specific nodes.

2. **Adjacency Matrix**
   * **Description**: An $n \times n$ matrix where $n$ is the number of nodes. A value of $1$ (or the weight) at position $(i, j)$ indicates an edge between node $i$ and node $j$.
   * **Pros**: Extremely fast ($O(1)$) to check if a direct connection exists between two nodes.
   * **Cons**: Consumes a lot of memory ($O(n^2)$), making it inefficient for large, sparse graphs.

3. **Edge List**
   * **Description**: The simplest representation. It consists of a list of all edges in the graph, with each edge represented as a pair of nodes.
   * **Pros**: Simple to implement and efficient for small graphs.
   * **Cons**: Inefficient for finding the neighbors of a given node.

In this repo, they are implemented using adjacency lists.

## Visualization Resources

For better understanding of graph concepts and algorithms:

* [Interactive Graph Data Structures](https://visualgo.net/en/graphds) - Visual representation of graph structures
* [Graph Traversal Algorithms](https://visualgo.net/en/dfsbfs) - Interactive visualization of DFS and BFS algorithms