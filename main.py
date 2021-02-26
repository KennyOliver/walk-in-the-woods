world = [
  ["","",""],
  ["","",""],
  ["","",""]
  ]
print(world)

world_map = {
  31: "7", 32: "8", 33: "9",
  21: "4", 22: "5", 23: "6",
  11: "1", 12: "2", 13: "3"
}
print(world_map.keys())

print("Proof of Concept!")

player_location = 22

for _ in range(0,3):
  print(f"You are at: {world_map[player_location]}")
  walk_direction = input("  N\nW + E\n  S\nEnter direction --> ").upper()
  if walk_direction == "N":
    player_location += 10
  elif walk_direction == "E":
    player_location += 1
  elif walk_direction == "S":
    player_location -= 10
  elif walk_direction == "W":
    player_location -= 1