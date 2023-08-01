"""
During my coding and exploration of GRAPH data structures, I questioned why BFS
employs a queue instead of other containers like a stack. I came across a valuable
link (https://stackoverflow.com/questions/39731498/why-does-the-bfs-algorithm-use-a-queue)
that shed light on the matter. The reason behind using a queue in BFS is that it operates
level by level, ensuring that sequential steps are followed and maintaining the correct
ordering of nodes. A queue ensures that nodes at the same level are processed before moving
to the next level, allowing BFS to traverse the graph breadth-first, exploring neighbor nodes
first before diving deeper. This characteristic makes a queue the ideal data structure for BFS,
as it effectively manages the ordering and maintains the desired exploration pattern.
BELOW CODE IS OF A BFS Traversal
"""
# Python3 Program to print BFS traversal from a given source vertex. BFS(int s) traverses vertices reachable from s.

from collections import defaultdict


# This class represents a directed graph
# using adjacency list representation
class Graph:

	# Constructor
	def __init__(self):

		# Default dictionary to store graph
		self.graph = defaultdict(list)

	# Function to add an edge to graph
	def addEdge(self, u, v):
		self.graph[u].append(v)

	# Function to print a BFS of graph
	def BFS(self, s):

		# Mark all the vertices as not visited
		visited = [False] * (max(self.graph) + 1)

		# Create a queue for BFS
		queue = []

		# Mark the source node as
		# visited and enqueue it
		queue.append(s)
		visited[s] = True

		while queue:

			# Dequeue a vertex from
			# queue and print it
			s = queue.pop(0)
			print(s, end=" ")

			# Get all adjacent vertices of the
			# dequeued vertex s.
			# If an adjacent has not been visited,
			# then mark it visited and enqueue it
			for i in self.graph[s]:
				if visited[i] == False:
					queue.append(i)
					visited[i] = True


# Driver code
if __name__ == '__main__':

	# Create a graph given in
	# the above diagram
	g = Graph()
	g.addEdge(0, 1)
	g.addEdge(0, 2)
	g.addEdge(1, 2)
	g.addEdge(2, 0)
	g.addEdge(2, 3)
	g.addEdge(3, 3)

	print("Following is Breadth First Traversal"
		" (starting from vertex 2)")
	g.BFS(2)

# This code is contributed by Neelam Yadav
