import math

#public keys
P = 23
G = 14

#private keys
a = 3
b = 4

Ka = (G**a) % P
Kb = (G**b) % P

symm_key_a = (Kb**a) % P
symm_key_b = (Ka**b) % P

print(Ka, Kb, symm_key_a, symm_key_b)