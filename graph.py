"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy
import pdb


'''
# Example Graph
   ___                     ___
 /     \                 /     \
|   1   | - - - - - - - |   3   |
 \ ___ /                 \ ___ /
    \         ___      /    |
     \      /     \   /     |
      \    |   5   | /      |
       \    \ ___ /  \      |
       ___            \    ___
     /     \           \ /     \
    |   2   |           |   4   |
     \ ___ /             \ ___ /



'''


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}  # this is our adjacency list

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        # quality check for possible duplicate vertice.
        if vertex_id in self.vertices:
            warning = f"WARNING: vert: {vertex_id} already exists!  No need to add the vert again."
            # print(warning)
            return warning
        else: 
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        # check if vertex exists
        if v1 in self.vertices and v2 in self.vertices:
            # add the edge
            self.vertices[v1].add(v2)
        else: 
            print(f"ERROR: Adding edge, vertex{v1} or vertex {v2} not found.")

    
    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        if vertex_id in self.vertices:
            return self.vertices[vertex_id]
        else:
            print(f"ERROR: No such vertex: {vertex_id}.")
            return None

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # create a queue and enque starting_vertex
        qq = Queue()
        qq.enqueue([starting_vertex])

        # start python debugger.  pdb.set_trace() 
        # breakpoint()
        # pdb.set_trace()

        # create a set of traversed vertices
        visited = set()
        # while queue is not empty:
        while qq.size() > 0:
            # dequeue/pop first vertex
            path = qq.dequeue()
            # if path not in visited:
            if path[-1] not in visited:
                # Do the thing
                print(path[-1])
                # add to visited
                visited.add(path[-1])
                # enqueue all neighbors
                for next_vert in self.get_neighbors(path[-1]):
                    new_path = list(path)
                    new_path.append(next_vert)
                    qq.enqueue(new_path)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # create a queue and enque starting_vertex
        ss = Stack()
        ss.push([starting_vertex])

        # start python debugger.  pdb.set_trace() 
        # breakpoint()
        # pdb.set_trace()

        # create a set of traversed vertices
        visited = set()
        # while queue is not empty:
        while ss.size() > 0:
            # dequeue/pop first vertex
            path = ss.pop() # <-- important to POP before anything else in the loop when using a stack or you can end up in an infinite loop.
            # if path not in visited:
            if path[-1] not in visited:
                # Do the thing
                print(path[-1])
                # add to visited
                visited.add(path[-1])
                # enqueue all neighbors
                for next_vert in self.get_neighbors(path[-1]):
                    new_path = list(path)
                    new_path.append(next_vert)
                    ss.push(new_path)

    def dft_recursive(self, starting_vertex, visited=None):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        # Initial Case
        if visited is None:
            visited = set()
        # Tracking Visited Verts
        if starting_vertex not in visited:
            print(starting_vertex)
            visited.add(starting_vertex)
            # Loop through neighboring verts, check if visited, recurse.
            for neighbor in self.get_neighbors(starting_vertex):
                # this is the break/base case
                if neighbor not in visited:
                    self.dft_recursive(neighbor, visited)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        qq = Queue()
        qq.enqueue([starting_vertex])  # this is enqueued as a list so we can add to the list.
        visited = set()

        while qq.size() > 0:
            # path is a list of the connected verts; initial pass it is just the starting vert. 
            path = qq.dequeue()

            # Do the thing!
            if path[-1] is destination_vertex:
                return path

            if path[-1] not in visited:
                visited.add(path[-1])

                for neighbor in self.get_neighbors(path[-1]):
                    new_path = path.copy()
                    new_path.append(neighbor)
                    qq.enqueue(new_path)



    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        ss = Stack()
        ss.push([starting_vertex])

        visited = set()

        while ss.size() > 0: 
            path = ss.pop()

            if path[-1] is destination_vertex:
                return path
            
            if path[-1] not in visited:
                visited.add(path[-1])

                for neighbor in self.get_neighbors(path[-1]):
                    new_path = path.copy()
                    new_path.append(neighbor)
                    ss.push(new_path)


    def dfs_recursive(self, starting_vertex, destination_vertex, visited=None, path=None):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        # Initial Case 1
        if visited is None:
            visited = set()
        # Initial Case 2
        if path is None:
            path = []

        # Track visited Nodes
        if starting_vertex not in visited:
            visited.add(starting_vertex)
            path_copy = path.copy()
            path_copy.append(starting_vertex)
        # Do the Thing; also one of our base/break cases
            if starting_vertex is destination_vertex:
                return path_copy    
        # Check for neighbors, recurse
            for neighbor in self.get_neighbors(starting_vertex):
                # Break Case
                new_path = self.dfs_recursive(neighbor, destination_vertex, visited, path_copy)
                # If there is a new_path, return it.  
                if new_path is not None:
                    return new_path


# if __name__ == '__main__':
#     graph = Graph()  # Instantiate your graph
#     # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
#     graph.add_vertex(1)
#     graph.add_vertex(2)
#     graph.add_vertex(3)
#     graph.add_vertex(4)
#     graph.add_vertex(5)
#     graph.add_vertex(6)
#     graph.add_vertex(7)
#     graph.add_edge(5, 3)
#     graph.add_edge(6, 3)
#     graph.add_edge(7, 1)
#     graph.add_edge(4, 7)
#     graph.add_edge(1, 2)
#     graph.add_edge(7, 6)
#     graph.add_edge(2, 4)
#     graph.add_edge(3, 5)
#     graph.add_edge(2, 3)
#     graph.add_edge(4, 6)

#     '''
#     Should print:
#         {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
#     '''
#     print(graph.vertices)

#     '''
#     Valid BFT paths:
#         1, 2, 3, 4, 5, 6, 7
#         1, 2, 3, 4, 5, 7, 6
#         1, 2, 3, 4, 6, 7, 5
#         1, 2, 3, 4, 6, 5, 7
#         1, 2, 3, 4, 7, 6, 5
#         1, 2, 3, 4, 7, 5, 6
#         1, 2, 4, 3, 5, 6, 7
#         1, 2, 4, 3, 5, 7, 6
#         1, 2, 4, 3, 6, 7, 5
#         1, 2, 4, 3, 6, 5, 7
#         1, 2, 4, 3, 7, 6, 5
#         1, 2, 4, 3, 7, 5, 6
#     '''
#     graph.bft(1)

#     '''
#     Valid DFT paths:
#         1, 2, 3, 5, 4, 6, 7
#         1, 2, 3, 5, 4, 7, 6
#         1, 2, 4, 7, 6, 3, 5
#         1, 2, 4, 6, 3, 5, 7
#     '''
#     graph.dft(1)
#     graph.dft_recursive(1)

#     '''
#     Valid BFS path:
#         [1, 2, 4, 6]
#     '''
#     print(graph.bfs(1, 6))

#     '''
#     Valid DFS paths:
#         [1, 2, 4, 6]
#         [1, 2, 4, 7, 6]
#     '''
#     print(graph.dfs(1, 6))
#     print(graph.dfs_recursive(1, 6))

# # import time

# # def test_set():
# #     start = time.time()
# #     myset = set([0,1,2,3,4,5])
# #     print("method set: ", type(myset))
# #     end = time.time()
# #     result = (end - start) * 1000
# #     print("method time: ", result)
# #     return result


# # def test_set_literal():
# #     start = time.time()
# #     myliteralset = {0,1,2,3,4,5}
# #     print("my literal set: ", type(myliteralset))
# #     end = time.time()
# #     result = (end - start) * 1000
# #     print("literal time: ", result)
# #     return result


# # test_set()
# # test_set_literal()