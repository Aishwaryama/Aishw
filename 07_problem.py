"""
??? Question with two examples ???
"""

import unittest


def decode_from_dict(dictionary):
    list = []
    for li in dictionary.keys():
        list.append(li)
    ll = []
    nn = []
    mm = [elem[1] for elem in dictionary.values()]
    total = 0
    for ele in range(0, len(mm)):
        total = total + mm[ele]
    for k in range(0, total):
        ll.append(0)
    for i in dictionary:
        for j in dictionary[i][0]:
            ll[j] = chr(i)
    str1 = ""    
    for ele in ll:  
        str1 += str(ele)

    return str1


# DO NOT TOUCH THE BELOW CODE
class TestDecodeFromDict(unittest.TestCase):

    def test_01(self):

        d = {112: [[0, 2], 2], 97: [[1, 3], 2]}
        output = "papa"

        self.assertEqual(decode_from_dict(d), output)

    def test_02(self):

        d = {107: [[0], 1], 114: [[1], 1], 97: [[2], 1], 110: [
            [3], 1], 116: [[4], 1], 104: [[5], 1], 105: [[6], 1]}
        output = "kranthi"

        self.assertEqual(decode_from_dict(d), output)

    def test_03(self):

        d = {84: [[0], 1], 104: [[1, 12], 2], 105: [[2, 9, 15], 3], 115: [[3, 10], 2], 32: [[4, 8, 11, 18], 4], 98: [[5], 1], 111: [
            [6, 20], 2], 120: [[7], 1], 97: [[13], 1], 118: [[14], 1], 110: [[16], 1], 103: [[17, 19], 2], 108: [[21], 1], 100: [[22], 1]}
        output = "This box is having gold"

        self.assertEqual(decode_from_dict(d), output)

    def test_04(self):

        d = {84: [[0], 1], 104: [[1], 1], 105: [[2, 10], 2], 115: [[3], 1], 32: [[4, 8], 2], 100: [
            [5], 1], 111: [[6], 1], 99: [[7], 1], 108: [[9], 1], 110: [[11], 1], 107: [[12], 1]}
        output = "This doc link"

        self.assertEqual(decode_from_dict(d), output)


if __name__ == '__main__':
    unittest.main(verbosity=2)
