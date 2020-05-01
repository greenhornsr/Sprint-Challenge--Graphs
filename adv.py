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

# BFS - used to find optimal path to destination!
def bfs(starting_vertex, destination_vertex):
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
            vert = path[-1]  # v2

            #breakdown destination:
            dest_vert = destination_vertex # v2

            # Do the thing!
            if vert is dest_vert:
                return path

            if vert not in visited:
                visited.add(vert)

                possexits = room_graph[vert][1]

                for neighbor in unvisited[vert]:
                    new_path = path.copy()
                    new_path.append(possexits[neighbor])  # v2
                    qq.enqueue(new_path)

# Recursive DFT
def dft_recursive(starting_vertex, visited=None, directions=None ):

    if visited is None:
        visited = set()

    if directions is None:
        directions = []

    invertd = [invert[dir] for dir in directions]

    if len(visited) < len(room_graph):
        #Directions/exits
        dir = unvisited[starting_vertex]
        exits_unknown = [exit for exit in dir if unvisited[starting_vertex][exit] == "?"]
        destination_vertex = 499
        if starting_vertex not in visited:
            visited.add(starting_vertex)

        if len(exits_unknown) >= 1:
            while starting_vertex is not destination_vertex:
                # choose random exit
                import random
                rand_index = random.randint(0,len(exits_unknown)-1)
                # Travel
                player.travel(exits_unknown[rand_index])
                traversal_path.append(exits_unknown[rand_index])
                directions.append(exits_unknown[rand_index])
                unvisited[starting_vertex][exits_unknown[rand_index]] = player.current_room.id
                unvisited[player.current_room.id][invert[traversal_path[-1]]] = starting_vertex
                # Recurse
                return dft_recursive(player.current_room.id, visited, directions)
            if starting_vertex is destination_vertex:
                # print(f"NO WHERE TO GO! \n{visited}\n")
                verts_remaining = [v for v in unvisited if v not in visited]
                if verts_remaining:
                    destination_vertex = verts_remaining[-1]
                return
            if len(visited) == len(room_graph):
                return traversal_path
            return dft_recursive(player.current_room.id, visited, directions)

        bfs(starting_vertex, len(room_graph)-1)

        if len(exits_unknown) == 0:
            # print("  ** NO EXITS!!")
            # print(f"    *** continuing on vert: {starting_vertex}")
            while starting_vertex is not destination_vertex:
                if invertd:
                    go_to = invertd[-1]
                    directions.pop()
                    player.travel(go_to)
                    traversal_path.append(go_to)
                    return dft_recursive(player.current_room.id, visited, directions)
            if starting_vertex is destination_vertex:
                # print(f"NO WHERE TO GO! \n{visited}\n")
                verts_remaining = [v for v in unvisited if v not in visited]
                if verts_remaining:
                    destination_vertex = verts_remaining[-1]
                return
            if len(visited) == len(room_graph):
                # print("ALL DONE!!!")
                return traversal_path
            return dft_recursive(player.current_room.id, visited, directions)
    return traversal_path

unvisited = create_unvisited(room_graph)
dft_recursive(0)
world.print_rooms()
# ************************* END DFT **************************



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
