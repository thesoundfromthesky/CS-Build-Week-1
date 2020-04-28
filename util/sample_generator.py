# Sample Python code that can be used to generate rooms in
# a zig-zag pattern.
#
# You can modify generate_rooms() to create your own
# procedural generation algorithm and use print_rooms()
# to see the world.


class Room:
    def __init__(self, id, name, description, x, y):
        self.id = id
        self.name = name
        self.description = description
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.x = x
        self.y = y
    def __repr__(self):
        if self.e_to is not None:
            return f"({self.x}, {self.y}) -> ({self.e_to.x}, {self.e_to.y})"
        return f"({self.x}, {self.y})"
    def connect_rooms(self, connecting_room, direction):
        '''
        Connect two rooms in the given n/s/e/w direction
        '''
        reverse_dirs = {"n": "s", "s": "n", "e": "w", "w": "e"}
        reverse_dir = reverse_dirs[direction]
        setattr(self, f"{direction}_to", connecting_room)
        setattr(connecting_room, f"{reverse_dir}_to", self)
    def get_room_in_direction(self, direction):
        '''
        Connect two rooms in the given n/s/e/w direction
        '''
        return getattr(self, f"{direction}_to")
    def get_connections(self):
      connections = 0
      if self.n_to is not None:
        connections += 1
      if self.e_to is not None:
        connections += 1
      if self.s_to is not None:
        connections += 1
      if self.w_to is not None:
        connections += 1

      



#### Start at corner 00
### Based upon the fact that connect_rooms needs a room object, need to do a full pass of all locations, create rooms, then do the pass to connect them.
## two directions aren't possible
## need to check if x == 0, or x == width // Blocks connections: y-1, x+1
## need to check if y == 0, or y == height // Blocks connections: x-1, y+1
## else
## roll all chances

## check if room has connection?? skip steps based on # of connections
## 100% to get first connection
## 85% to get second connection
## 60% to get third
## 10% to get 4th


## can_n: y-1, x == 0
## can_e: x+1, x == width
## can_s: y+1, y == height
## can_w: x-1, y == 0

## if x == width,
## reset position to x=0, y+=1, 
## else x += 1

## repeat until done




class World:
  def __init__(self):
    self.grid = None
    self.width = 0
    self.height = 0
  def generate_rooms(self, size_x, size_y, num_rooms):
    '''
    Fill up the grid, bottom to top, in a zig-zag pattern
    '''

    # Initialize the grid
    self.grid = [None] * size_y
    self.width = size_x
    self.height = size_y
    for i in range( len(self.grid) ):
      self.grid[i] = [None] * size_x
    print(self.grid)

    # Start from lower-left corner (0,0)
    x = 0
    y = 0
    room_count = 0
    indexed_height = height-1
    indexed_width = width-1

    # # Start generating rooms by line until max height/width reached

    ###### Creating All Rooms
    while room_count < num_rooms:
      ## start left to right, incrementing x by 1, until x = width
      ## reset x, y+1
      ## need to create first room:
      if x == 0 and y == 0:
        print('first if')
        print(x, y)
        room = Room(room_count, "A Generic Room", "This is a generic room.", x, y)
        self.grid[y][x] = room
        x += 1
        room_count = room_count + 1

        print(x, y)
      ## Create exit case of last room
      elif y < indexed_height and x == indexed_width:
        print('first elif')
        print(x, y)
        room = Room(room_count, "A Generic Room", "This is a generic room.", x, y)
        self.grid[y][x] = room
        y += 1
        x = 0
        room_count = room_count + 1
        print(x, y)
      elif x < indexed_width:
        print('second elif')
        print(x, y)
        room = Room(room_count, "A Generic Room", "This is a generic room.", x, y)
        self.grid[y][x] = room
        x += 1
        room_count = room_count + 1
        print(x, y)
      elif y == indexed_height and x == indexed_width:
        print('LAST ONE')
        print(x, y)
        room = Room(room_count, "A Generic Room", "This is a generic room.", x, y)
        self.grid[y][x] = room
        print(room_count, num_rooms)
        room_count = room_count+1
      else:
        print('Ive fucked something')

    ## reset variables
    # room_count = 0
    # x = 0
    # y = 0

    print('rooms created')
    print(self.grid)
    print(self.grid[3][4].x)

### helper for directions
    ## can_n: y-1, x == 0
    ## can_e: x+1, x == width
    ## can_s: y+1, y == height
    ## can_w: x-1, y == 0
    
    ### Now that rooms are created, we can connect them randomly
    for row in self.grid:
      for room in row:
        x = room.x
        y = room.y
        connections = room.get_connections()

    
    ## get room of room_count ---- Could try the reverse grid section (without reversing) to go row by row in grid

    ## can_n: True
    ## can_e: True
    ## can_s: True
    ## can_w: True
    ## call get_connections
      ## need to check if x == 0, or x == width // Blocks connections: y-1, x+1
      ## need to check if y == 0, or y == height // Blocks connections: x-1, y+1
      # for each that are considered Blocked, add +1 to connections
      # flip can_#: False for blocked directions/current directions

    ## Roll random(int) to determine # of connections that will be made.

    #if random is 4 connections:
      # room.connect_rooms(????????, n) (x, y+1)
      # room.connect_rooms(?????, e)





      # if x < width:
        
      #   x += 1
      #   room_count = room_count + 1
      # elif y < height and x == width:
      #   y += 1
      #   x = 0
      #   room_count = room_count + 1
      # elif x < width:
      #   room = Room(room_count, "A Generic Room", "This is a generic room.", x, y)
      #   x += 1
      #   room_count = room_count + 1
      # elif y == height and x == width:
      #   pass



###################OLD
    # direction = 1  # 1: east, -1: west


    # # While there are rooms to be created...
    # #??? Do I need this?? What is this initializing???
    # while room_count < num_rooms:

    #   # 
    #   # Need to create edge/corner cases to ensure it doesn't try to connect to things that aren't there
    #   # 
    #   if direction > 0 and x < size_x - 1:
    #     room_direction = "e"
    #     x += 1
    #   elif direction < 0 and x > 0:
    #     room_direction = "w"
    #     x -= 1
    #   else:
    #     # If we hit a wall, turn north and reverse direction
    #     room_direction = "n"
    #     y += 1
    #     direction *= -1

    #   # Create a room in the given direction
    #   room = Room(room_count, "A Generic Room", "This is a generic room.", x, y)
    #   # Note that in Django, you'll need to save the room after you create it

      # Save the room in the World grid




      #### OLD
      # # Connect the new room to the previous room
      # if previous_room is not None:
      #   previous_room.connect_rooms(room, room_direction)

      # # Update iteration variables
      # previous_room = room
      # room_count += 1



  def print_rooms(self):
    '''
    Print the rooms in room_grid in ascii characters.
    '''

    # Add top border
    str = "# " * ((3 + self.width * 5) // 2) + "\n"

    # The console prints top to bottom but our array is arranged
    # bottom to top.
    #
    # We reverse it so it draws in the right direction.
    reverse_grid = list(self.grid) # make a copy of the list
    reverse_grid.reverse()
    for row in reverse_grid:
        # PRINT NORTH CONNECTION ROW
        str += "#"
        for room in row:
            if room is not None and room.n_to is not None:
                str += "  |  "
            else:
                str += "     "
        str += "#\n"
        # PRINT ROOM ROW
        str += "#"
        for room in row:
            if room is not None and room.w_to is not None:
                str += "-"
            else:
                str += " "
            if room is not None:
                str += f"{room.id}".zfill(3)
            else:
                str += "   "
            if room is not None and room.e_to is not None:
                str += "-"
            else:
                str += " "
        str += "#\n"
        # PRINT SOUTH CONNECTION ROW
        str += "#"
        for room in row:
            if room is not None and room.s_to is not None:
                str += "  |  "
            else:
                str += "     "
        str += "#\n"

    # Add bottom border
    str += "# " * ((3 + self.width * 5) // 2) + "\n"

    # Print string
    print(str)


w = World()
width = 10
height = 10
num_rooms = width * height
w.generate_rooms(width, height, num_rooms)
w.print_rooms()


print(f"\n\nWorld\n  height: {height}\n  width: {width},\n  num_rooms: {num_rooms}\n")
