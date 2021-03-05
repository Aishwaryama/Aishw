# decode base 3 to integer
"""
A navy head command is preparing itself to attack the terrorist installations. 
There is a large fleet waiting to attack, and restrain until further orders.

The head quarters has given each enemy installation a code number. If they send these
details directly to the on frontline commander, they might get in the hands of
enemy message interpreters.

for this they are sending a list of numbers (as strings) which are of base 3 and your task is to
decode them to decimal numbers and written the list.

Example:


"""

import unittest
import math

def decode_base_three(nums):
    a = []
    for k in nums:
        N = int(k)
        if (N != 0): 
            decimalNumber = 0;  
            i = 0; 
            remainder = 0; 
            while (N != 0): 
                remainder = N % 10; 
                N = N // 10; 
                decimalNumber += remainder * math.pow(3, i); 
                i += 1; 
            
            a.append(decimalNumber)
        
        else: 
            a.append(0)
    return a

class TestDecodeBaseThree(unittest.TestCase):

    def test_01(self):
        l = ['10', '20', '21']
        output_nums = [3, 6, 7]

        self.assertEqual(decode_base_three(l), output_nums)

    def test_02(self):
        l = ['10', '20', '21', '11', '100']
        output_nums = [3, 6, 7, 4, 9]

        self.assertEqual(decode_base_three(l), output_nums)

    def test_03(self):
        l = ['10', '101', '210', '11', '100']
        output_nums = [3, 10, 21, 4, 9]

        self.assertEqual(decode_base_three(l), output_nums)


if __name__ == '__main__':
    unittest.main(verbosity=2)
