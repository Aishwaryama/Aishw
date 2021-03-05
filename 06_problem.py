# Encode the Text
"""
Given a text as string, encode this string as dictionary

rules: The dictionary should contain the ASCII value of the character as key and a list of (list of positions) and total count of the character as corresponding value
Example 1
Input

s = "coco"

Output

d= {99 : [[0,2], 2], 111 : [[1,3], 2] }


"""
import unittest


def encoding_to_dict(s):
    li = []
    for el in s:
        li.append(ord(el))
    test_list = list(set(li)) 
    dic = {}
    for l in test_list:
        res_list = [] 
        for i in range(0, len(li)) : 
            if li[i] == l : 
                res_list.append(i) 
        dic[l] = [res_list]
        dic[l].append(len(res_list))
    return dic

class TestEncodeToDict(unittest.TestCase):

    def test_01(self):
        s = "papa"
        output = {112: [[0, 2], 2], 97: [[1, 3], 2]}

        self.assertEqual(encoding_to_dict(s), output)

    def test_02(self):
        s = "kranthi"
        output = {107: [[0], 1], 114: [[1], 1], 97: [[2], 1], 110: [
            [3], 1], 116: [[4], 1], 104: [[5], 1], 105: [[6], 1]}

        self.assertEqual(encoding_to_dict(s), output)

    def test_03(self):
        s = "This box is having gold"
        output = {84: [[0], 1], 104: [[1, 12], 2], 105: [[2, 9, 15], 3], 115: [[3, 10], 2], 32: [[4, 8, 11, 18], 4], 98: [[5], 1], 111: [
            [6, 20], 2], 120: [[7], 1], 97: [[13], 1], 118: [[14], 1], 110: [[16], 1], 103: [[17, 19], 2], 108: [[21], 1], 100: [[22], 1]}

        self.assertEqual(encoding_to_dict(s), output)

    def test_04(self):
        s = "This doc link"
        output = {84: [[0], 1], 104: [[1], 1], 105: [[2, 10], 2], 115: [[3], 1], 32: [[4, 8], 2], 100: [
            [5], 1], 111: [[6], 1], 99: [[7], 1], 108: [[9], 1], 110: [[11], 1], 107: [[12], 1]}

        self.assertEqual(encoding_to_dict(s), output)


if __name__ == '__main__':
    unittest.main(verbosity=2)
