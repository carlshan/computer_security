"""
Implementation of RSA algorithm by Rivest, Shamir and Adleman

RSA Algorithm:
* choose two prime numbers, p and q. These should be large.
* compute n = p * q
* choose your encryption key, e, such that e and n are relatively prime
* find the corresponding decryption key, d, such at e * d is 1 when mod n
* to encrypt a number N, your encrypted message M is N**e mod n
* to decrypt M back to N, evaluate M**d mod n
"""
import random
import unittest

primes = [
    5915587277,
    1500450271,
    3267000013,
    5754853343,
    4093082899,
    9576890767,
    3628273133,
    2860486313,
    5463458053,
    3367900313,
]


def find_encrypt_key(p, q):
    """
    Finds e such that e and (p-1) * (q-1) are relatively prime.
    """
    phi = (p-1) * (q-1)
    encrypt_key = random.randrange(1, phi)
    g = gcd(encrypt_key, phi)
    while g != 1:
        encrypt_key = random.randrange(1, phi)
        g = gcd(encrypt_key, phi)
    return encrypt_key


def find_decrypt_key(encrypt_key, phi):
    """
    Finds d such that (d * e + 1) is divisible by phi
    """
    for d in range(3, phi, 2):
        if d * encrypt_key % phi == 1:
            return d


def are_relatively_prime(a, b):
    # returns True if a and b are relatively prime. False otherwise.
    # To be relatively prime means that there are no common prime factors
    # between the two numbers outside of 1.
    return gcd(a, b) == 1


# source: http://stackoverflow.com/questions/11175131/code-for-greatest-common-divisor-in-python
def gcd(a, b):
    """
    Returns the greatest common denominator between two numbers, a and b.
    """
    while b != 0:
        a, b = b, a % b
    return a

def xor(a, b):
    new = []
    for x, y in zip(a, b):
        if int(x) + int(y) == 1:
            new.append('1')
        else:
            new.append('0')
    return ''.join(new)

class PublicKey:

    def __init__(self, encrypt_key, n):
        self.encrypt_key = encrypt_key
        self.n = n

    def encrypt(self, number):
        return pow(number, self.encrypt_key, self.n)


class PrivateKey:

    def __init__(self, decrypt_key, n):
        self.decrypt_key = decrypt_key
        self.n = n

    def decrypt(self, number):
        return pow(number, self.decrypt_key, self.n)


class TestRSA(unittest.TestCase):
    # Tests from
    # http://code.activestate.com/recipes/578838-rsa-a-simple-and-easy-to-read-implementation/

    def test_known_results(self):
        public = PublicKey(n=2534665157, encrypt_key=7)
        private = PrivateKey(n=2534665157, decrypt_key=1810402843)

        self.assertEqual(public.encrypt(123), 2463995467)
        self.assertEqual(public.encrypt(456), 2022084991)
        self.assertEqual(public.encrypt(123456), 1299565302)
        self.assertEqual(private.decrypt(2463995467), 123)
        self.assertEqual(private.decrypt(2022084991), 456)
        self.assertEqual(private.decrypt(1299565302), 123456)


if __name__ == '__main__':
    unittest.main()
