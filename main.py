world_map = {
  71:"T", 72:"T", 73:"H", 74:"T", 75:"T", 76:"W", 77:"W",
  61:"T", 62:"T", 63:"T", 64:"H", 65:"T", 66:"T", 67:"W",
  51:"T", 52:"T", 53:"W", 54:"T", 55:"M", 56:"T", 57:"W",
  41:"W", 42:"W", 43:"H", 44:"$", 45:"T", 46:"M", 47:"M",
  31:"W", 32:"W", 33:"W", 34:"H", 35:"T", 36:"M", 37:"H",
  21:"H", 22:"W", 23:"W", 24:"W", 25:"H", 26:"T", 27:"H",
  11:"T", 12:"T", 13:"T", 14:"H", 15:"H", 16:"H", 17:"T"
}
#print(world_map.keys())

compass = "/ N \ \nW + E\n\ S /"
print("<-- Walk In The Woods -->")
print("A 7x7 world made from a dictionary!")
print("<-- Info -->\n$ = spawn point\nT = tree\nW = water\nH = house\nM = mountain")

player_location = 44 #initial location (i.e. spawn point)

print("-" * 20)
print(compass)

while True:
  display_location = world_map.get(player_location, " ")
  north_object = world_map.get(player_location + 10, " ")
  east_object = world_map.get(player_location + 1, " ")
  south_object = world_map.get(player_location - 10, " ")
  west_object = world_map.get(player_location - 1, " ")
  
  adjacent_objects = f"* {north_object} *\n{west_object} {display_location} {east_object}\n* {south_object} *"
  print("-" * 20)
  print(adjacent_objects)
  
  walk_direction = input("Go --> ").upper()
  while walk_direction not in ["N","E","S","W"]:
    walk_direction = input("Invalid --> ").upper()
    print("\033[A                             \033[A") #clear previous line
  
  if walk_direction == "N":
    player_location += 10
  elif walk_direction == "E":
    player_location += 1
  elif walk_direction == "S":
    player_location -= 10
  elif walk_direction == "W":
    player_location -= 1
  
  print("\033[A                             \033[A") #clear previous lines
  print("\033[A                             \033[A") #need space to remove previous console input
  print("\033[A                             \033[A")
  print("\033[A                             \033[A")
  print("\033[A                             \033[A")
  #print("\033[A\033[A" * 3)