f = open("depth.txt", 'rt')
depths = []
for line in f:
  depths.append(int(line.strip()))
  
increased = 0
for i in range(3, len(depths)):
  print(sum(depths[i-4:i-1]))
  increased += 1 if sum(depths[i-3:i]) < sum(depths[i-2:i+1]) else 0
print(increased)
f.close()