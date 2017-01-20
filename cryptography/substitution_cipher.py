"""
Simple Caesar cipher implementation
"""
import unittest


def encrypt(message, shift_n):
    """
    Encrypts a message via shifting position of each letter by shift_n
    """
    # mod 256 due to ASCII encoding
    shifted = [chr(_encrypt_helper(letter, shift_n) % 256)
                                                    for letter in message]
    encrypted = ''.join(shifted)
    return encrypted


def _encrypt_helper(letter, shift_n):
    """
    Shifts integer ordinal position of a letter by shift_n
    """
    return ord(letter) + shift_n


class SubstitutionTestCase(unittest.TestCase):

    shift_1 = {
        "carl": 'dbsm',
        "Carl": 'Dbsm',
        "This is a sentence.": "Uijt!jt!b!tfoufodf/",
        "Encrypt me!": "Fodszqu!nf\"",
        }

    shift_256 = {k: k for k in shift_1}

    def test_shift_by_256(self):
        shift_n = 256
        for message in self.shift_256:
            correct = self.shift_256[message]
            self.assertEqual(encrypt(message, shift_n), correct)

    def test_shift_by_1(self):
        shift_n = 1
        for message in self.shift_1:
            correct = self.shift_1[message]
            self.assertEqual(encrypt(message, shift_n), correct)

if __name__ == '__main__':
    unittest.main()
