def get_points(x, y):
  if len(x) != len(y):
    return []
  points = []
  for i in range(len(x)):
    points.append((x[i], y[i]))
  return points

x = [1, 2, 3, 4, 5] p
y = [6, 7, 8, 9, 10] 
points = get_points(x, y) 
print(points) 

