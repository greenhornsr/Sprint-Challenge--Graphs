# PROCESS
    # put SV into visited
    # Check sv for possible Exits that do not equal "?" and put into array
    # if there is an exit and the exit hasn't been visited, travel
    # no exit; BFS for nearest vert that has an exit.
    # repeat.
    # if all verts have been visited (500), DONE!





# paste all of below in the My Code Section of adv.py
print('room graph: ')
print(room_graph)

print("\n")
print(f"Starting Room Name: {player.current_room.name}\n")
print(f"Starting Room ID: {player.current_room.id}\n")

print("\n")
print("player current room exits: ")
print(f"exits: {player.current_room.get_exits()[0]}\n")
for exit in player.current_room.get_exits():
    traversal_path.append(exit)

print("\n")
print("travel direction: ")
print(f"traveling: {player.current_room.get_exits()[0]}")
player.travel(player.current_room.get_exits()[0])
for exit in player.current_room.get_exits():
    traversal_path.append(exit)

print("\n")
print(f"exits for room: {player.current_room.id}, {player.current_room.get_exits()}")
print(f"traveling: {player.current_room.get_exits()[0]}")
player.travel(player.current_room.get_exits()[0])
for exit in player.current_room.get_exits():
    traversal_path.append(exit)

print("\n")
print(f"Next Room ID: {player.current_room.id}")
print("exits: ", player.current_room.get_exits())






## DFT-RECURSIVE
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


# MISC CODE ATTEMPTS
# queue for vert/room (i.e. 0)
# qv = [start_vert]
# # queue for exits/direction (i.e. West to room 1, {w:1})
# qe = []

# # Vert/room
# visited_r = set()
# # exit/direction
# visited_e = set()

# # travel = player.travel(direction)

# while len(qv) > 0:
#     vert = qv.pop()

#     if vert not in visited_r:
#         visited_r.add(vert)
#         exits = player.current_room.get_exits()
#         print("vert", vert)

#         if exits:
#             for exit in exits:
#                 # print("exit", exit)
#                 # print(unvisited[vert][exit])
#                 if unvisited[vert][exit] == '?':
#                     # qe.append(exit)
#                     player.travel(exit)
#                     vert = player.current_room.id
#                     print("vert", vert)


#                     # while len(qe) > 0: 
#                     #     print("qe: ", qe)
#                     #     dir = qe.pop()
#                     #     print("direction: ", dir)
#                     #     # player.travel(dir)
#                     #     print("id", player.current_room.id)

#                         # if dir not in visited_e:

## LATEST ATTEMPT>...traverses...but not well:
# def dft_recursive(starting_vert, visited=None):
#     """
#     Print each vertex in depth-first order
#     beginning from starting_vertex.

#     This should be done using recursion.
#     """
#     # Initial Case
#     if visited is None:
#         visited = set()
#     # Tracking Visited Verts
#     if starting_vert not in visited:
#         print("starting vert: ", starting_vert)
#         visited.add(starting_vert)
#         # exits
#         exits = player.current_room.get_exits()
#         # print(f"exits: {exits}")
#         # unvisited[starting_vert] = {exit:'?' for exit in exits}
#         print("unvisited: ", unvisited)

#         while len(exits) > 0:
#             dir = exits.pop()
#             print('exit: ', dir)


#             if unvisited[starting_vert][dir] == '?':
#                 conn_room = unvisited[starting_vert][dir]
#                 print("CONN_ROOM: ", conn_room)
#                 if conn_room == '?':
#                     print("oops\n")
#                     player.travel(dir)
#                     next_room = player.current_room.id
#                     unvisited[starting_vert][dir] = next_room

#                 # for neighbor in unvisited[starting_vert]:
#                 #     # this is the break/base case
#                 #     print(f"direction: {neighbor}")
#                 #     # print(f"neighbor: {unvisited[starting_vert][dir]}")
#                 if next_room not in visited:
#                     print("next room: ", next_room)
#                     dft_recursive(next_room, visited)


# dft_recursive(s_v)

## LATEST ATTEMPT  ....
# print('room graph: ')
# for k, v in room_graph.items():
#     print(k, v[1])

# # Creating unvisited dict/graph.  To track visited, populate the unvisited ? with a vert.  Once all ? is exchanged for a vert # done!

# # Inversed DIRECTIONS dict:
# invert = {"n":"s", "e":"w", "s":"n", "w":"e"}

# def maze_traveler(s_v, prev_room=None, unvisited = None, visited = None):

#     if unvisited is None:
#         unvisited = {k:v for (k,v) in room_graph.items()}
#         for room, vals in unvisited.items():
#             unvisited[room] = vals[1]
#             for k,val in vals[1].items():
#                 # print(k, val)
#                 vals[1][k] = '?' 
#         print("unvisited: ")    
#         print(unvisited)

#     if prev_room is None:
#         prev_room = player.current_room.id

#     if visited is None:
#         visited = set({s_v})

#     # get exits
#     print("Starting room", s_v)
#     exits = [exit for exit in unvisited[s_v] if exit != "?"]
#     print("CURRENT EXITS: ", exits)
#     route = exits[0]


#     # Choosing Route
#     if len(exits) > 1:
#         route = exits[random.randint(1, len(exits)-1)]
#         # print(f"EXIT Choice: {the_exit}, EXIT DIRECTION: {exits[the_exit]}")
    
#         # check for next room
#         next_room = player.current_room.get_room_in_direction(route)

#         print("ROUTE: ", route)
#         print("NEXT ROOM: ", next_room.id)
#         print("unvisited: ", unvisited)
        
#         if next_room and next_room.id not in visited:
#             visited.add(next_room.id)
#             print("visited: ", visited)

#             # Update unvisited
#             unvisited[s_v][route] = next_room.id

#             # hold the prev room
#             prev_room = s_v

#             # if unvisited[s_v][route] == "?":
#             print("Route: ", route)

#             # travel and append the route(direction)
#             player.travel(route)
#             traversal_path.append(route)
#             unvisited[player.current_room.id][invert[route]] = s_v

#             print("traversal path: ", traversal_path)
#             print("Moving to: ", player.current_room.id, "\n\n")
            
#             maze_traveler(player.current_room.id, prev_room, unvisited, visited)

#         print("wha brotha?")

#     if route == exits[0]:
#         # print("PREV ROOM: ", prev_room)
#         # print("ONLY Route: ", route)
#         print("route 0 unvisited: ", unvisited)


#         # Begin BFS
#         # def bfs(self, starting_vertex, destination_vertex):
#         qq = []
#         qq.append([s_v])  # this is enqueued as a list so we can add to the list.
#         visited_paths = set()

#         while len(qq) > 0:
#             # path is a list of the connected verts; initial pass it is just the starting vert. 
#             path = qq.pop()
#             print("path", path)
#             print("path", path[-1])

#             # Do the thing!
#             # if path[-1] is destination_vertex:
#             #     return path

#             if path[-1] not in visited_paths:
#                 visited_paths.add(path[-1])

#                 for neighbor in unvisited[path[-1]]:
#                     # print("Neighbor: ", neighbor)
#                     print("dkalfjda", unvisited[path[-1]])
#                     new_path = path.copy()
#                     if unvisited[path[-1]][neighbor] is not "?":
#                         new_path.append(unvisited[path[-1]][neighbor])
#                         qq.append(new_path)
#                     else:
#                         print("WTF?")
#                         # unvisited[path[-1]][neighbor] == "?":
#                         # player.travel(path[-1])
#                         # maze_traveler(path[-1], prev_room, unvisited, visited)






# maze_traveler(player.current_room.id)


# # ****** helper func ********
# def get_destination(curr_room = None, new_path_copy=None):
#     new_path_copy = path.copy()
#     print(f"{new_path_copy}")
#     print("Remember to pop this from new_path_copy? Room", new_path_copy[-1])
#     dest = new_path_copy[-1] 
#     print(f"current room before traveling: {player.current_room.id}\n")
#     end_exits = player.current_room.get_exits()
#     print(f"room Exits: {end_exits}")
#     if len(end_exits) == 1:
#         player.travel(end_exits[-1])
#         new_path_copy.pop()
#         print(f"  ** only {len(end_exits)} exit!")
#         print(f"  ** traveled to: {player.current_room.id}")
#         traversal_path.append(end_exits[-1])
#         print(f"  ** traveler path: {traversal_path}\n\n")
#         curr_room = player.current_room.id
#         get_destination(curr_room, new_path_copy)
#     for exit in end_exits:
#         print(f"room Exits: {end_exits}")
#         print(f"VERT EXITS: {unvisited[curr_room][exit]}")
#         print(f'current vert: {dest}, exit: {exit}')
#         if unvisited[curr_room][exit] == '?':
#             new_path_copy.pop()
#             player.travel(exit)
#             traversal_path.append(end_exits[-1])
#             print(f"  ** traveler path: {traversal_path}\n\n")
#             get_destination(curr_room, new_path_copy)

#         new_path_copy.pop()
#         player.travel(exit)
#         get_destination(curr_room, new_path_copy)
#         traversal_path.append(end_exits[-1])
#         print(f"  ** traveler path: {traversal_path}\n\n")
#     return dest

#     # return dest
# get_destination()
# # ******* END HELPER ********