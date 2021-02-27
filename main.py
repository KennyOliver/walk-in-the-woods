world_map = {
  71:"T", 72:"T", 73:"T", 74:"T", 75:"T", 76:"0", 77:"W",
  61:"T", 62:"0", 63:"T", 64:"0", 65:"T", 66:"T", 67:"W",
  51:"T", 52:"0", 53:"0", 54:"0", 55:"M", 56:"T", 57:"0",
  41:"W", 42:"W", 43:"H", 44:"S", 45:"T", 46:"M", 47:"M",
  31:"W", 32:"W", 33:"W", 34:"0", 35:"T", 36:"M", 37:"H",
  21:"H", 22:"W", 23:"W", 24:"0", 25:"0", 26:"T", 27:"H",
  11:"T", 12:"T", 13:"T", 14:"H", 15:"H", 16:"H", 17:"T"
}
#print(world_map.keys())

compass = "/ N \ \nW + E\n\ S /"
print("<-- Walk In The Woods -->")
print("<-- Info -->\nS = spawn point\nT = tree\nW = water\nH = house\nM = mountain\n0 = nothing")

player_location = 44 #initial location (i.e. spawn point)

print("-" * 20)
print(compass)

while True:
  display_location = world_map.get(player_location, "V")
  north_object = world_map.get(player_location + 10, "V")
  east_object = world_map.get(player_location + 1, "V")
  south_object = world_map.get(player_location - 10, "V")
  west_object = world_map.get(player_location - 1, "V")
  
  adjacent_objects = f"* {north_object} *\n{west_object} {display_location} {east_object}\n* {south_object} *"
  print("-" * 20)
  print(adjacent_objects)
  
  walk_direction = input("Go --> ").upper()
  while walk_direction not in ["N","E","S","W"]:
    walk_direction = input("Enter compass direction --> ").upper()
    print ("\033[A\033[A")
  
  if walk_direction == "N":
    player_location += 10
  elif walk_direction == "E":
    player_location += 1
  elif walk_direction == "S":
    player_location -= 10
  elif walk_direction == "W":
    player_location -= 1
  
  print ("\033[A\033[A" * 3) #clear previous lines
  #print ("\033[A                             \033[A")