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



# print('room graph: ')
# for k, v in room_graph.items():
#     print(k, v[1])

# Creating unvisited dict/graph.  To track visited, populate the unvisited ? with a vert.  Once all ? is exchanged for a vert # done!
def create_unvisited(graph):
    import copy

    unvisited = copy.deepcopy(graph)
    for room, vals in unvisited.items():
        unvisited[room] = vals[1]
        for k,val in vals[1].items():
            # print(k, val)
            vals[1][k] = '?' 
    # print("unvisited: ")    
    # print(unvisited)
    return unvisited

# ****** END HELPER ******

# from graph import Graph
# DFT
from util import Stack, Queue

# Inversed DIRECTIONS dict:
invert = {"n":"s", "e":"w", "s":"n", "w":"e"}

# Starting Vert/Edge
start_vert = player.current_room.id
# edges = unvisited[start_vert]


# ************************** DFT **************************
# start python debugger.  pdb.set_trace() 
# breakpoint()
# pdb.set_trace()

# DECLARE BFS - used to find optimal path to destination!
def bfs(starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        qq = Queue()
        # qq.enqueue([(starting_vertex[0], starting_vertex[1])])  # this is enqueued as a list so we can add to the list.  # v1
        qq.enqueue([starting_vertex])  # this is enqueued as a list so we can add to the list.  # v2
        visited = set()

        while qq.size() > 0:
            # path is a list of the connected verts; initial pass it is just the starting vert. 
            path = qq.dequeue()
            # vert = path[-1][0]  # v1
            vert = path[-1]  # v2

            #breakdown destination:
            # dest_vert = destination_vertex[0] # v1
            dest_vert = destination_vertex # v2

            # Do the thing!
            if vert is dest_vert:
                return path

            if vert not in visited:
                visited.add(vert)

                possexits = room_graph[vert][1]

                for neighbor in unvisited[vert]:
                    new_path = path.copy()
                    # new_path.append((possexits[neighbor], neighbor))   # v1
                    new_path.append(possexits[neighbor])  # v2
                    qq.enqueue(new_path)

# DECLARE DFT 
def dft_recursive(starting_vertex, visited=None, lap_path=None):
    """
    Print each vertex in depth-first order
    beginning from starting_vertex.

    This should be done using recursion.
    """
    # Initial Case
    if visited is None:
        visited = set()

    if lap_path is None:
        lap_path = []


    #Starting Vert Check:
    print(f"\n\nStarting ROOM: {starting_vertex}")
    print(f"PLAYER CURRENT ROOM: {player.current_room.id}")

    # Tracking Visited Verts
    if starting_vertex not in visited:
        visited.add(starting_vertex)

        # GET/MANAGE EXITS
        # dir = player.current_room.get_exits()
        # exits = [e for e in dir if unvisited[starting_vertex][e] is "?"]
        exits = player.current_room.get_exits()
        # exits = unvisited[starting_vertex]
        print(f"  ** ROOM: {player.current_room.id} Player EXITS: {exits}")
        # print(f"  ** TESTEXITS: {testexits}")

        # Loop through neighboring verts, check if visited, recurse.
        for next_vert in exits:
            # print("exits: ", player.current_room.get_exits())
            print("  ** next vert: ", next_vert)

            # this is the break/base case
            if next_vert in unvisited[starting_vertex]: 
                if room_graph[starting_vertex][1][next_vert] not in visited:
                    print(f"  ** From {starting_vertex}, checking {next_vert} and found: {room_graph[starting_vertex][1][next_vert]}.")
                    # if unvisited[starting_vertex][next_vert] not in visited:
                    print("  ** next room: ", room_graph[starting_vertex][1][next_vert])
                    lap_path.append(next_vert)
                    print("path is: ", lap_path)
                    dft_recursive(room_graph[starting_vertex][1][next_vert], visited, lap_path)
            print(f"  ** FINISHED LOOP!")
        print(f"Exiting starting vert in visited!")
    print(f"FINISHED RECURSIVE LAP! \n")

# # TRAVEL?
# prev_vert = starting_vertex
# player.travel(exits[-1])
# traversal_path.append(exits[-1])
# unvisited[starting_vertex][exits[-1]] = player.current_room.id
# unvisited[player.current_room.id][invert[exits[-1]]] = starting_vertex

unvisited = create_unvisited(room_graph)
dft_recursive(0)



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
