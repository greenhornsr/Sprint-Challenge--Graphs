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


# DFT 
# def dft(starting_vertex):
#         """
#         Print each vertex in depth-first order
#         beginning from starting_vertex.
#         """
#         # create a queue and enque starting_vertex
#         ss = Stack()
#         ss.push([(starting_vertex, None)])

#         # create a set of traversed vertices
#         visited = set()
#         # while queue is not empty:
#         while ss.size() > 0:
#             print("\n88 - CURRENT ROOM: ", player.current_room.id)
            
#             # dequeue/pop first vertex
#             path = ss.pop() # <-- important to POP before anything else in the loop when using a stack or you can end up in an infinite loop.
#             print("  ** 92 - PATH:", path)
#             print(f"  ** 93 - current path: {path[-1]}")
#             vert, dir = path[-1]
#             # print("VERT: ", vert)
#             # if path not in visited:
            
#             # print("STACK: ", ss.stack)

#             if vert not in visited:     
#                 # add to visited
#                 visited.add(vert)
#                 # print("VISITED: ", visited)
#                 #            
#                 # Do the thing
#                 if dir is not None: 
#                     print(f"  ** 103 - Now Exploring vert: {vert}")
#                     possible_exits = player.current_room.get_exits()
#                     print(f"possible exits: {possible_exits}")
#                     for exit in possible_exits: 
#                         print(f"\n    ** 106 - prev vert: {path[-2]}")
#                         print(f"\n    ** 107 - prev vert exits: {unvisited[path[-2][0]]}")
#                         print(f"\n    ** 108 - prev vert exit vert: {unvisited[path[-2][0]][exit]}")
#                         if unvisited[path[-2][0]][exit] in visited and unvisited[path[-2][0]][exit] is not None:
#                             # destination vert
#                             # if ss.size() > 0:
#                             previous_vert = ss.stack[-1][1]
#                             # print("PREVIOUS VERT", previous_vert)
#                             optimal_path = bfs(path[-1], previous_vert)[::-1]
#                             optimal_path.pop()
#                             print("\n    ** 116 - OPTIMAL PATH: ", optimal_path)
#                             ss.stack = ss.stack + [optimal_path]

#                             print(f"    ** 119 - STACK: {ss.stack}")
    
#                         # WHEN DO I WANT TO TRAVEL?
#                         '''
#                             scenario 1: when a room has unexplored exits
#                             scenario 2: when reaching a dead end (no unexplored verts) & len(visited < 500), reverse course
#                         '''

#                         # SCENARIO 1: 
#                         # print(f"CURRENT unvisited: ", unvisited[vert])
#                         player.travel(dir) # uses letter direction
#                         traversal_path.append(dir) # update where I travelled
#                         print(f"    ** 128 - I moved {traversal_path[-1]} to ROOM: {player.current_room.id}")
#                         print(f"129 - CURRENT ROOM IS NOW: {player.current_room.id}")
#                         unvisited[vert][invert[dir]] = path[-2][0]
#                         unvisited[path[-2][0]][dir] = vert
#                         # print("travelled path: ", traversal_path)
#                         # print(f"Previous UNVISITED: ", unvisited[path[-2][0]])                    


#                 # enqueue all neighbors
#                 for next_vert in unvisited[vert]:
#                     myexits = room_graph[vert][1]
#                     print("STACK UP THE NEIGHBOR: ", myexits[next_vert], next_vert)
#                     # print("exits: ",myexits[next_vert])
#                     if unvisited[vert][next_vert] == "?":
#                         new_path = list(path)
#                         new_path.append((myexits[next_vert], next_vert))
#                         ss.push(new_path)
#                         # print(f"unvisited: ", unvisited)
#                 # print("stack: ", ss.stack)
#                 print(f"LAP FINISHED!  \n\n")

# BFS - used to find optimal path to destination!
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



# unvisited = create_unvisited(room_graph)
# dft(0)


# Recursive DFT
def dft_recursive(starting_vertex, visited=None, directions=None ):
    # print("unvisited: ", unvisited)

    if visited is None:
        visited = set()

    if directions is None:
        directions = []

    invertd = [invert[dir] for dir in directions]

    # print(f"212 - Starting VERT: {starting_vertex}")
    if len(visited) < len(room_graph):
        #Directions
        dir = unvisited[starting_vertex]
        exits_unknown = [exit for exit in dir if unvisited[starting_vertex][exit] == "?"]
        # exits_known = player.current_room.get_exits()
        destination_vertex = 499
        # print(f"  ** 219 - exits: {exits_unknown}")
        if starting_vertex not in visited:
            visited.add(starting_vertex)

        if len(exits_unknown) >= 1:
            while starting_vertex is not destination_vertex:
                # choose random exit
                import random
                rand_index = random.randint(0,len(exits_unknown)-1)
                # print("random index: ", rand_index)
                # print(f"  ** exits: {exits_unknown}")
                player.travel(exits_unknown[rand_index])
                traversal_path.append(exits_unknown[rand_index])
                directions.append(exits_unknown[rand_index])
                # print(f"  ** I moved {traversal_path[-1]} to ROOM: {player.current_room.id}")
                unvisited[starting_vertex][exits_unknown[rand_index]] = player.current_room.id
                unvisited[player.current_room.id][invert[traversal_path[-1]]] = starting_vertex
                return dft_recursive(player.current_room.id, visited, directions)
            if starting_vertex is destination_vertex:
                # print(f"NO WHERE TO GO! \n{visited}\n")
                verts_remaining = [v for v in unvisited if v not in visited]
                # print(f"unvisited verts: \n{verts_remaining}")
                if verts_remaining:
                    destination_vertex = verts_remaining[-1]
                    # return dft_recursive(player.current_room.id, visited, directions)
                return
            if len(visited) == len(room_graph):
                # print("ALL DONE!!!")
                return traversal_path
            return dft_recursive(player.current_room.id, visited, directions)

        bfs(starting_vertex, 499)

        # elif len(visited) < 500:
        if len(exits_unknown) == 0:
            # print("  ** NO EXITS!!")
            # print(f"    *** continuing on vert: {starting_vertex}")
            while starting_vertex is not destination_vertex:
                # print("NEWDIRS: ", invertd)
                if invertd:
                    go_to = invertd[-1]
                    directions.pop()
                    # print(f"GOING: {go_to}")
                    player.travel(go_to)
                    # print("NEWDIRS after POP: ", invertd)
                    traversal_path.append(go_to)
                    return dft_recursive(player.current_room.id, visited, directions)
            # player.current_room.get_exits()
            if starting_vertex is destination_vertex:
                # print(f"NO WHERE TO GO! \n{visited}\n")
                verts_remaining = [v for v in unvisited if v not in visited]
                # print(f"unvisited verts: \n{verts_remaining}")
                if verts_remaining:
                    destination_vertex = verts_remaining[-1]
                    # return dft_recursive(player.current_room.id, visited, directions)
                return
            if len(visited) == len(room_graph):
                # print("ALL DONE!!!")
                return traversal_path
            return dft_recursive(player.current_room.id, visited, directions)

    # print("visited: ", visited)
    # print(f"END OF THE ROAD!  Room: {starting_vertex} only has no unexplored exit: {unvisited[starting_vertex]}")
    # print("START VERT: ", starting_vertex)
    # mypath = [vert for vert in visited]
    # print(f"UNVISITED: \n{unvisited}")
    # print(f"MORE TO DO?  {directions}")
    return traversal_path

    # # TEST! 
    # if len(exits_known) > 1:
    # for exit in exits_known:
    #     possible_exit = room_graph[starting_vertex][1][exit]
    #     print("??AFDSAFADFA?????: ", possible_exit)
    #     if possible_exit not in visited:
    #         player.travel(exit)
    #         traversal_path.append(exit)
    #         directions.append(exit)
    #         print(f"  ** I moved {traversal_path[-1]} to ROOM: {player.current_room.id}")
    #         unvisited[starting_vertex][exit] = player.current_room.id
    #         unvisited[player.current_room.id][invert[traversal_path[-1]]] = starting_vertex
    #         return dft_recursive(player.current_room.id, visited, directions)   


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
