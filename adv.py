from room import Room
from player import Player
from world import World

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
# map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []
#*******************************MY CODE*******************************



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

from graph import Graph
# DFT
from util import Stack

# Inversed DIRECTIONS dict:
invert = {"n":"s", "e":"w", "s":"n", "w":"e"}

# Starting Vert/Edge
start_vert = player.current_room.id
edges = unvisited[start_vert]


g = Graph()
################DFT################
"""
Print each vertex in depth-first order
beginning from starting_vertex.
"""
# create a queue and enque starting_vertex
ss = Stack()
ss.push([start_vert])

# start python debugger.  pdb.set_trace() 
# breakpoint()
# pdb.set_trace()

# create a set of traversed vertices
visited = set()
prev_room = player.current_room.id
# while queue is not empty:
while ss.size() > 0:
    # dequeue/pop first vertex
    path = ss.pop() # <-- important to POP before anything else in the loop when using a stack or you can end up in an infinite loop.
    print("path: ", path)

    # if path not in visited:
    if path[-1] not in visited:
        # add to visited
        visited.add(path[-1])
        print(f"path: {path[-1]}")

        # ***** Do the thing *****
        dir = player.current_room.get_exits()
        exits = [exit for exit in dir if unvisited[path[-1]][exit] == "?"]
        print("exits", exits)
        print("vert", unvisited[path[-1]][dir[-1]])

        if exits and unvisited[path[-1]][exits[-1]] == "?":
            print(f"current room: {player.current_room.id}, dir is {exits[-1]}")
            print("vert", unvisited[path[-1]][exits[-1]])
            print("path: ", path)
            print("path: ", path[-1])
            player.travel(exits[-1])
            traversal_path.append(exits[-1])
            print("path again: ", path)            
            print("path again: ", path[-1])
            unvisited[path[-1]][exits[-1]] = player.current_room.id
            print(f"updated vert: {path[-1]}, dir: {exits[-1]} to be {unvisited[path[-1]][exits[-1]]}")

            unvisited[player.current_room.id][invert[exits[-1]]] = prev_room
            prev_room = player.current_room.id
            # print(f"current room: ", player.current_room.id)
            # print(f"unvisited again: ", unvisited)
            # enqueue all neighbors
            for next_vert in unvisited[path[-1]]:
                if unvisited[path[-1]][next_vert] != "?" and next_vert != invert[exits[-1]]:
                    print("UNVISITED>>.: ", unvisited)
                    print("next vert", next_vert)
                    print("#EFWFE", unvisited[path[-1]][next_vert],"\n\n\n")
                    new_path = list(path)
                    new_path.append(unvisited[path[-1]][next_vert])
                    ss.push(new_path)





# ************ END DFT *************


# BFS
from util import Queue








#*****************************END MY CODE*****************************



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
