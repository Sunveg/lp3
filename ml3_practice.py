import math

points = [
[ [2,4] , [4,6] , [4,2] , [6,4] ], #blue
[ [4,4] , [6,2] ] #orange
]

k = 3

p = [6,6]

distance = []

for i in range(2):
	for pair in points[i]:
		euclidean_distance = math.sqrt((pair[0]-p[0])**2 + (pair[1]-p[1])**2)
		distance.append((euclidean_distance, i))

f0 = 0
f1 = 0

distance = sorted(distance)[0:k]
print(distance)

for d in distance:
	if d[1] == 1:
		f1 = f1 + 1
	else:
		f0 = f0 + 1

print("KNN:\n")
if f0>f1:
	print("The point [6,6] is : Blue")
else:
	print("The point [6,6] is : Orange")

fr0 = 0
fr1 = 0

print("\nWeighted KNN:\n")

for d in distance:
	if d[1] == 1:
		fr1 = fr1 + (1/d[0])
	else:
		fr0 = fr0 + (1/d[0])

if fr0>fr1:
	print("The point [6,6] is : Blue")
else:
	print("The point [6,6] is : Orange")

