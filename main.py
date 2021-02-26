world = [
  ["","",""],
  ["","",""],
  ["","",""]
  ]
#print(world)

world_map = {
  51:"T", 52:"N", 53:"N", 54:"N", 55:"T",
  41:"N", 42:"N", 43:"H", 44:"N", 45:"T",
  31:"H", 32:"T", 33:"C", 34:"N", 35:"N",
  21:"N", 22:"T", 23:"X", 24:"N", 25:"N",
  11:"T", 12:"T", 13:"T", 14:"H", 15:"N"
}
#print(world_map.keys())

print("Proof of Concept!")

compass = "  N\nW + E\n  S"
player_location = 33 #initial location (i.e. spawn point)

print("Info: C = center; T = tree; H = house; N = nothing")

while True:
  print(compass)
  try:
    print(f"You are at: {world_map[player_location]}")
  except KeyError:
    print("YOU ARE IN THE VOID! GO BACK!")
  walk_direction = input("Enter direction --> ").upper()
  if walk_direction == "N":
    player_location += 10
  elif walk_direction == "E":
    player_location += 1
  elif walk_direction == "S":
    player_location -= 10
  elif walk_direction == "W":
    player_location -= 1