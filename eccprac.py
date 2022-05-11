import random, math

def point(a, b):
	if 4*(a**3) + 27*(b**2) != 0:
		x = 1
		print("generating")
		while True:
			rhs = x**3 + a*x + b
			y = int(math.sqrt(rhs))
			lhs = y**2
			if lhs == rhs:
				return [x, y]
			else:
				x += 1
	else:
		print('choose another points')

private_a = 13
private_b = 15

a = int(input('enter a: '))
b = int(input('enter b: '))

generator = point(a, b)
print('generator point: ', generator)

m = int(input('enter plaintext: '))

public_a = [private_a*generator[0], private_a*generator[1]]
public_b = [private_b*generator[0], private_b*generator[1]]

k = 3

c1 = k*(generator[0] + generator[1])

c2 = m + k*(public_b[0]) + k*(public_b[1])

ct = [c1, c2]

print('ciphertext is: ', ct)

r = private_b * c1

pt = c2 - r

print('plaintext is: ', pt)