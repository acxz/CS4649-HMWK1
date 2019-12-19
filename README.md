# CS4649-HMWK1
Implementations of depth-first search (DFS), breadth-first search (BFS), and
iterative-deepening search (IDS) compared based on time, paths popped frome
queue, max queue size, and path length. The algorithms are tested on a graph of
USA with MA as the starting vertex and GA as the goal vertex.

## Descriptions
`dfs.py`: file that contains the DFS algorithm

`bfs.py`: file that contains the BFS algorithm

`ids.py`: file that contains the IDS algorithm

`graph.py`: file that contains the graph class used in this assignment

`main.py`: file that runs all the searches on the specified graph (USA) with the
specified start and goal nodes (MA, GA)

## Dependencies
 - Python 3 [Python Download](https://www.python.org/downloads/)

## Run
To test these algorithms, run the `main.py` file like so:

    python3 main.py

`main.py` will call each search from its respective file and output the
information as required by Problem 1 in Homework 1

