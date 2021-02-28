world_map = {
  71:"░", 72:"░", 73:"■", 74:"░", 75:"░", 76:"▒", 77:"▒",
  61:"░", 62:"░", 63:"░", 64:"■", 65:"░", 66:"░", 67:"▒",
  51:"░", 52:"░", 53:"▒", 54:"▒", 55:"Λ", 56:"░", 57:"▒",
  41:"▒", 42:"▒", 43:"■", 44:"$", 45:"▒", 46:"Λ", 47:"Λ",
  31:"▒", 32:"▒", 33:"▒", 34:"■", 35:"▒", 36:"Λ", 37:"■",
  21:"■", 22:"▒", 23:"▒", 24:"▒", 25:"■", 26:"▒", 27:"■",
  11:"▒", 12:"▒", 13:"▒", 14:"■", 15:"■", 16:"■", 17:"▒"
}
#print(world_map.keys())

compass = "╔ N ╗ \nW + E\n╚ S ╝"
print("<-- Walk In The Woods -->")
print("A 7x7 world made from a dictionary!\nYou have an aerial view")
print("<-- Info -->")
print("$ = spawn-point\n▒ = tree\n░ = water\n■ = house\nΛ = mountain")

player_location = 44 #spawn-point

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