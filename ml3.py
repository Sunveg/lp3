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
		e_dist = math.sqrt((pair[0] - p[0])**2 + (pair[1] - p[1])**2)
		distance.append((e_dist, i))

f0 = 0
f1 = 0

distance = sorted(distance)[:k]

for d in distance:
	if d[1] == 1:
		f1 += 1
	else:
		f0 += 1

print('normal knn:')
if f0>f1:
	print('blue')
else:
	print('orange')

fr0 = 0
fr1 = 0

for d in distance:
	if d[1] == 1:
		fr1 += 1/d[0]
	else:
		fr0 += 1/d[0]

print('\ndist weighted knn:')
if fr0>fr1:
	print('blue')
else:
	print('orange')
