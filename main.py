world_map = {
  51:"T", 52:"0", 53:"0", 54:"0", 55:"T",
  41:"0", 42:"0", 43:"H", 44:"0", 45:"T",
  31:"H", 32:"T", 33:"C", 34:"0", 35:"0",
  21:"0", 22:"T", 23:"T", 24:"0", 25:"0",
  11:"T", 12:"T", 13:"T", 14:"H", 15:"0"
}
#print(world_map.keys())

compass = "  N\nW + E\n  S"
print("<-- Walk In The Woods -->")
print("<-- Info -->\nC = center\nT = tree\nH = house\n0 = nothing")

player_location = 33 #initial location (i.e. spawn point)

while True:
  ''' try:
    print(f"You\'re at:\t{world_map[player_location]}")
  except KeyError:
    print("YOU\'RE IN THE VOID - GO BACK!") '''
  
  try:
    display_location = world_map[player_location]
  except KeyError:
    display_location = "V"
  try:
    north_object = world_map[player_location + 10]
  except KeyError:
    north_object = "V"
  try:
    east_object = world_map[player_location + 1]
  except KeyError:
    east_object = "V"
  try:
    south_object = world_map[player_location - 10]
  except KeyError:
    south_object = "V"
  try:
    west_object = world_map[player_location - 1]
  except KeyError:
    west_object = "V"
  #adjacent_objects = f"  {world_map[player_location + 10]}\n{world_map[player_location - 1]} {world_map[player_location]} {world_map[player_location + 1]}\n  {world_map[player_location - 10]}"
  adjacent_objects = f"  {north_object}\n{west_object} {display_location} {east_object}\n  {south_object}"
  print("-" * 30)
  print(compass)
  print("\n")
  print(adjacent_objects)
  
  walk_direction = input("Go --> ").upper()
  while walk_direction not in ["N","E","S","W"]:
    walk_direction = input("Enter compass direction --> ").upper()
  
  if walk_direction == "N":
    player_location += 10
  elif walk_direction == "E":
    player_location += 1
  elif walk_direction == "S":
    player_location -= 10
  elif walk_direction == "W":
    player_location -= 1