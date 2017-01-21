#Key Generation steps
 - Choose a L-bit prime p, such that it satifies the following
	- 512 <= L <= 1024
	- 64 divides L
	- p-1 has a 160-bit prime factor, eg. q.
 - Choose a g that belongs to group Zp* such that order of g is q.
 - Choose a number uniformly at random from set {2,3,...,q-1}.
 - Compute h = g^a mod p. (using square and multiply)
 - Verification Key = (p,q,g,h)
 - Signing key = a

#Signing process
The input to this algorithm is a message-file F, verification key and signing key. The output is the signature on file in signature.txt.
 - Choose a random element r in 1 <= r <= q-1
 - Compute C1 = ( g^r mod p) mod q. (using square and multiply)
 - Compute C2 = (int(SHA1(F)) + aC1)r^-1 mod q. (r^-1 using extended Euclidean algorithm)
 - If C1=0 or C2=0, a new random value of r should be chosen and C1, C2 to be recomputed.
 - Output (C1, C2) as signature on the file F.

#Verification process
The input to this algorithm is a message-signature pair (F, (C1, C2)) and the VerKey (p, q, g, h).
 - Compute t1 = int(SHA1(F))C2^-1 mod q. (C2^-1 using extended Euclidean algorithm)
 - Compute t1 = C1C2^-1 mod q.
 - if (g^t1 * h^t2 mod p) mod q = C1 then output "valid signature" else output "invalid signature".

python version : 3.4.3