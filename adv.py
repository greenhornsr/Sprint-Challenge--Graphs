from room import Room
from player import Player
from world import World

import pdb
import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []
#************************************** MY CODE **************************************



print('room graph: ')
for k, v in room_graph.items():
    print(k, v[1])

# Creating unvisited dict/graph.  To track visited, populate the unvisited ? with a vert.  Once all ? is exchanged for a vert # done!
unvisited = {k:v for (k,v) in room_graph.items()}
for room, vals in unvisited.items():
    unvisited[room] = vals[1]
    for k,val in vals[1].items():
        # print(k, val)
        vals[1][k] = '?' 
print("unvisited: ")    
print(unvisited)

# ****** END HELPER ******

# from graph import Graph
# DFT
from util import Stack

# Inversed DIRECTIONS dict:
invert = {"n":"s", "e":"w", "s":"n", "w":"e"}

# Starting Vert/Edge
start_vert = player.current_room.id
edges = unvisited[start_vert]


# g = Graph()
# ************************** DFT **************************
"""
Print each vertex in depth-first order
beginning from starting_vertex.
"""
'''
        2

        1

8   7   0   3   4

        5

        6
    
- start_vert is 0, 
- add start_vert to stack
- create visited tracker array.
- while stack size greather than 0:
    - pop last item from stack into path variable
    - check if last item is in visited array.
    - check if last item/path  has neighbors with '?'
        - if it h

- 0:{n:?, s:?, e:?, w:?}
    if 0: direction = ?
        travel n
    else: 
        travel back to 0

'''


# start python debugger.  pdb.set_trace() 
# breakpoint()
# pdb.set_trace()

def dft_recursive(starting_vertex, visited=None, directions=None ):
    # print("unvisited: ", unvisited)

    if visited is None:
        visited = set()

    if directions is None:
        directions = []

    invertd = [invert[dir] for dir in directions]

    dir = player.current_room.get_exits()
    exits = [exit for exit in dir if unvisited[starting_vertex][exit] == "?"]
    destination_vertex = 0
    # print(f"exits: {unvisited[4]}")

    print(f"Starting VERT: {starting_vertex}")

    # if starting_vertex not in visited:
    #     visited.add(starting_vertex)

    if len(exits) >= 1:
        print(f"  ** exits: {exits}")
        player.travel(exits[-1])
        traversal_path.append(exits[-1])
        directions.append(exits[-1])
        print(f"  ** I moved {traversal_path[-1]} to ROOM: {player.current_room.id}")
        unvisited[starting_vertex][exits[-1]] = player.current_room.id
        unvisited[player.current_room.id][invert[traversal_path[-1]]] = starting_vertex
        return dft_recursive(player.current_room.id, visited, directions)

    # reverse course: 
    elif len(exits) == 0 and starting_vertex is not destination_vertex:
        print("NEWDIRS: ", invertd)
        go_to = invertd[-1]
        directions.pop()
        print(f"GOING: {go_to}")
        player.travel(go_to)
        print("NEWDIRS after POP: ", invertd)
        traversal_path.append(go_to)
        return dft_recursive(player.current_room.id, visited, directions)

    print(f"END OF THE ROAD!  Room: {starting_vertex} only has no unexplored exit: {unvisited[starting_vertex]}")
    print("START VERT: ", starting_vertex)
    print("visited: ", visited)
    # mypath = [vert for vert in visited]
    # return mypath
    print(f"UNVISITED: \n{unvisited}")
dft_recursive(0)



# ************************* END DFT **************************

# **************************** BFS ****************************
from util import Queue

def bfs(starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        
        qq = Queue()
        qq.enqueue([starting_vertex[-1]])  # this is enqueued as a list so we can add to the list.
        visited = set(starting_vertex)

        while qq.size() > 0:
            # path is a list of the connected verts; initial pass it is just the starting vert. 
            path = qq.dequeue()
            print("Path: ", path)
            print("Path: ", path[-1])
            # Do the thing!
            if path[-1] is destination_vertex:
                print("DONE!!")
                return path

            if path[-1] not in visited:
                visited.add(path[-1])
                print("VISITED: ", visited)

                for neighbor in unvisited[path[-1]]:
                    print(neighbor)
                    new_path = path.copy()
                    new_path.append(unvisited[path[-1]][neighbor])
                    qq.enqueue(new_path)

# dft_recursive(0)
# bfs(dft_recursive(0),0)
print('path travelled: ', traversal_path)

# def bfs(starting_vertex, destination_vertex):
#         """
#         Return a list containing the shortest path from
#         starting_vertex to destination_vertex in
#         breath-first order.
#         """
#         print("qq starting vert: ", starting_vertex[0])
#         qq = Queue()
#         qq.enqueue(starting_vertex)  # this is enqueued as a list so we can add to the list.
#         bfs_visited = set()

#         while qq.size() > 0:
#             # path is a list of the connected verts; initial pass it is just the starting vert. 
#             bfs_path = qq.dequeue()
#             # while qt.size() > 0:
#             # print("I went: ", bfs_path)
#             print('\nFULL BFS_path', bfs_path)
#             print('BFS path[-1]', bfs_path[-1])
#             # Do the thing!
#             if bfs_path[-1] is destination_vertex:
#                 print(f"WE FINALLY GOT to the DESTINATION - {destination_vertex}")
#                 print(f"bfs_path @ destination vert {destination_vertex}: {bfs_path}")
#                 return bfs_path

#             elif bfs_path[-1] not in bfs_visited:
#                 bfs_visited.add(bfs_path[-1])
#                 print(f"bfs_visited: {bfs_visited}")
#                 # Do the thing.
#                 # traversal_path.append()
#                 # print(f"original path: {traversal_path}")
    
#                 for next_vert in unvisited[bfs_path[-1]]:
#                     if unvisited[bfs_path[-1]] == "?":
#                         print(f"FOUND ONE!", unvisited[bfs_path[-1]])
#                     qq_new_path = path.copy()
#                     qq_new_path.pop()
#                     # qq_new_path.append(unvisited[bfs_path[-1]][next_vert])
#                     print("next vert: ", next_vert)
#                     print(f"hello mcfly: {unvisited[bfs_path[-1]][next_vert]}")
#                     qq.enqueue(qq_new_path)


# bfs(new_path[::-1], traversal_path[0])


# ************************* END BFS **************************

# ************************************ END MY CODE ************************************



# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")



#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
