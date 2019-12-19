# Author: Akash Patel

from graph import Graph
from dfs import dfs
from bfs import bfs
from ids import ids

# Create the USA graph

USA = {'CA': ['AZ', 'NV', 'OR'],
       'WA': ['OR', 'ID'],
       'OR': ['WA', 'CA', 'NV', 'ID'],
       'NV': ['OR', 'CA', 'AZ', 'UT', 'ID'],
       'ID': ['WA', 'OR', 'NV', 'UT', 'WY', 'MT'],
       'UT': ['ID', 'NV', 'AZ', 'CO', 'WY'],
       'AZ': ['UT', 'NV', 'CA', 'NM'],
       'MT': ['ID', 'WY', 'SD', 'ND'],
       'WY': ['MT', 'ID', 'UT', 'CO', 'NE', 'SD'],
       'CO': ['WY', 'UT', 'NM', 'OK', 'KS', 'NE'],
       'NM': ['CO', 'AZ', 'TX', 'OK'],
       'ND': ['MT', 'SD', 'MN'],
       'SD': ['ND', 'MT', 'WY', 'NE', 'IA', 'MN'],
       'NE': ['SD', 'WY', 'CO', 'KS', 'MO', 'IA'],
       'KS': ['NE', 'CO', 'OK', 'MO'],
       'OK': ['KS', 'CO', 'NM', 'TX', 'AR', 'MO'],
       'TX': ['OK', 'NM', 'LA', 'AR'],
       'MN': ['ND', 'SD', 'IA', 'WI'],
       'IA': ['MN', 'SD', 'NE', 'MO', 'IL', 'WI'],
       'MO': ['IA', 'NE', 'KS', 'OK', 'AR', 'TN', 'KY', 'IL'],
       'AR': ['MO', 'OK', 'TX', 'LA', 'MS', 'TN'],
       'LA': ['AR', 'TX', 'MS'],
       'WI': ['MN', 'IA', 'IL', 'MI'],
       'IL': ['WI', 'IA', 'MO', 'KY', 'IN'],
       'MS': ['AR', 'LA', 'AL', 'TN'],
       'MI': ['WI', 'IN', 'OH'],
       'IN': ['MI', 'IL', 'KY', 'OH'],
       'KY': ['IN', 'IL', 'MO', 'TN', 'VA', 'WV', 'OH'],
       'TN': ['KY', 'MO', 'AR', 'MS', 'AL', 'GA', 'NC', 'VA'],
       'AL': ['TN', 'MS', 'FL', 'GA'],
       'OH': ['MI', 'IN', 'KY', 'WV', 'PA'],
       'WV': ['OH', 'KY', 'VA', 'MD', 'PA'],
       'VA': ['WV', 'KY', 'TN', 'NC', 'DC', 'MD'],
       'GA': ['TN', 'AL', 'FL', 'SC', 'NC'],
       'FL': ['GA', 'AL'],
       'PA': ['OH', 'WV', 'MD', 'DE', 'NJ', 'NY'],
       'MD': ['PA', 'WV', 'VA', 'DC', 'DE'],
       'DC': ['MD', 'VA'],
       'NC': ['VA', 'TN', 'GA', 'SC'],
       'SC': ['NC', 'GA'],
       'VT': ['NY', 'MA', 'NH'],
       'NY': ['VT', 'PA', 'NJ', 'CT', 'MA'],
       'NJ': ['NY', 'PA', 'DE'],
       'DE': ['NJ', 'PA', 'MD'],
       'NH': ['VT', 'MA', 'ME'],
       'MA': ['NH', 'VT', 'NY', 'CT', 'RI'],
       'CT': ['MA', 'NY', 'RI'],
       'ME': ['NH'],
       'RI': ['MA', 'CT'],
      }

USAGraph = Graph(USA)
startVertex = 'MA'
goalVertex = 'GA'

# DFS
[Dtime, DpathsPopped, DmaxQSize, Dpath] = dfs(USAGraph, startVertex, goalVertex)

# BFS
[Btime, BpathsPopped, BmaxQSize, Bpath] = bfs(USAGraph, startVertex, goalVertex)

# IDS
[Itime, IpathsPopped, ImaxQSize, Ipath] = ids(USAGraph, startVertex, goalVertex)

print("Search, [Time (s), # Paths Popped from Queue, Max Queue Size, Returned Path's Length/Cost], Path")
print("DFS, " + str([Dtime, DpathsPopped, DmaxQSize, len(Dpath) - 1]) + ", " +
        str(Dpath))
print("BFS, " + str([Btime, BpathsPopped, BmaxQSize, len(Bpath) - 1]) + ", " +
        str(Bpath))
print("IDS, " + str([Itime, IpathsPopped, ImaxQSize, len(Ipath) - 1]) + ", " +
        str(Ipath))
