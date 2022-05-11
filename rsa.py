import math

p = 11
q = 3

n = p*q

phi_n = (p-1)*(q-1)

#calculate e
e = 2
while e<phi_n:
	if math.gcd(e, phi_n) == 1:
		break
	e += 1

#calculate d
k = 1
while (k*phi_n + 1)%e != 0:
	k += 1
d = (k*phi_n + 1)//e

public_key = [e, n]
private_key = [d, n]

plaintext = 89

def encrypt(P, U):
	e, n = U
	C = (P**e) % n
	return C

def decrypt(C, U):
	d, n = U
	P = (C**d) % n
	return P

ciphertext = encrypt(plaintext, public_key)
pt = decrypt(ciphertext, private_key)

print(ciphertext, pt)

