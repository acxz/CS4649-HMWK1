# Author: Akash Patel

from graph import Graph
from datetime import datetime

def bfs(graph, startVertex, goalVertex):
    start = datetime.now()
    pathsPopped = 0
    maxQSize = 0
    path = []

    # 1. Initialize Q with a partial path <S>; set Visited = {}
    Q = [[startVertex]]
    visitedList = [startVertex]
    N = []
    # 2. If Q is empty, fail. Else, pick a partial path N from Q
    while True:
        if not Q:
            end = datetime.now()
            time = end - start
            time_sec = time.total_seconds()
            return [str(time_sec), pathsPopped, maxQSize, 'N/A']
        else:
            N = Q[0]
        # 3. If head(N) = G, return N   // Goal reach!
        if N[-1] == goalVertex:
            pathsPopped = pathsPopped + 1
            path = N
            end = datetime.now()
            time = end - start
            time_sec = time.total_seconds()
            return [str(time_sec), pathsPopped, maxQSize, path]
        # 4. Else:
        else:
        #   a) Remove N from Q
            Q.pop(0)
            pathsPopped = pathsPopped + 1
        #   b) Find all children of head(N) not in Visited and create a on-step extension of N to
        #   each child
            allChildrenHeadN = graph.adjacencyList(N[-1])
            allChildrenHeadNNotInVisited = [x for x in allChildrenHeadN if x not in visitedList]

            # Sort children alphabetically
            allChildrenHeadNNotInVisited.sort()

        #   c) Add all extended paths to Q
            for child in allChildrenHeadNNotInVisited:
                extendedPath = N.copy()
                extendedPath.append(child)
                Q.append(extendedPath)
            if len(Q) > maxQSize:
                maxQSize = len(Q)

        #   d) Add Children of head(N) to visited
            visitedList.extend(allChildrenHeadNNotInVisited)

        #   e) GOTO step 2
        #   Just have a while loop always running and the return statements should
        #   handle the terminating case
