world_map = {
  51:"T", 52:"N", 53:"N", 54:"N", 55:"T",
  41:"N", 42:"N", 43:"H", 44:"N", 45:"T",
  31:"H", 32:"T", 33:"C", 34:"N", 35:"N",
  21:"N", 22:"T", 23:"T", 24:"N", 25:"N",
  11:"T", 12:"T", 13:"T", 14:"H", 15:"N"
}
#print(world_map.keys())

print("<-- Walk In The Woods -->")
compass = "  N\nW + E\n  S"
print("<-- Info -->\nC = center\nT = tree\nH = house\nN = nothing")

player_location = 33 #initial location (i.e. spawn point)

while True:
  print("-" * 30)
  print(compass)
  try:
    print(f"You\'re at:\t{world_map[player_location]}")
  except KeyError:
    print("YOU\'RE IN THE VOID - GO BACK!")
  try:
    print(f"North is:\t{world_map[player_location + 10]}")
  except KeyError:
    print("North is:\tVOID!")
  try:
    print(f"East is:\t{world_map[player_location + 1]}")
  except KeyError:
    print("East is:\tVOID!")
  try:
    print(f"South is:\t{world_map[player_location - 10]}")
  except KeyError:
    print("South is:\tVOID!")
  try:
    print(f"West is:\t{world_map[player_location - 1]}")
  except KeyError:
    print("West is:\tVOID!")
  
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