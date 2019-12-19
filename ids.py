# Author: Akash Patel

from graph import Graph
from datetime import datetime

def ids(graph, startVertex, goalVertex):
    start = datetime.now()
    pathsPopped = 0
    maxQSize = 0
    path = []

    # Counter for the max depth increases every iteration in the for loop
    # Yeah using a flag would be nice but this is good enough for the assignment
    for i in range(1, 99999999):
        # 1. Initialize Q with a partial path <S>; set Visited = {}
        Q = [[startVertex]]
        visitedList = [startVertex]
        N = []
        # 2. If Q is empty, fail. Else, pick a partial path N from Q
        j = 0
        # Need to make this while loop based on whether Q is not empty so that
        # we can exit after everything is popped
        while Q:
            N = Q[-1]
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
                Q.pop(-1)
                pathsPopped = pathsPopped + 1
            #   b) Find all children of head(N) not in Visited and create a on-step extension of N to
            #   each child
                # Keep track of how deep to add children based on the current
                # iteration
                if (j < i - 1):
                    allChildrenHeadN = graph.adjacencyList(N[-1])
                    j = j + 1
                    allChildrenHeadNNotInVisited = [x for x in allChildrenHeadN if x not in visitedList]

                    # Sort children alphabetically
                    allChildrenHeadNNotInVisited.sort(reverse=True)

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
            #   Just have a while loop always while queue is not empty and the
            #   return statements should handle the terminating case

    end = datetime.now()
    time = end - start
    time_sec = time.total_seconds()
    return [str(time_sec), pathsPopped, maxQSize, 'N/A']
