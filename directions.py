f = open("directions.txt", 'rt')
directions = []
tally = {"forward": 0, "depth": 0, "aim": 0}
for line in f:
  directions.append(line)

for direction in directions:
  commands = direction.split(" ")
  if commands[0] == "forward":
    tally["forward"] += int(commands[1])
    tally["depth"] += tally["aim"] * int(commands[1])
  if commands[0] == "up":
    # tally["depth"] -= int(commands[1])
    tally["aim"] -= int(commands[1])
  if commands[0] == "down":
    # tally["depth"] += int(commands[1])
    tally["aim"] += int(commands[1])

print(tally["forward"] * tally["depth"])