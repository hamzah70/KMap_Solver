# CSE 101 - IP HW2
# K-Map Minimization 
# Name : MOHAMMAD HAMZAH AKHTAR
# Roll Number : 2018051	
# Section : A
# Group : 3

import unittest
from HW2_2018051 import minFunc
from HW2_2018051 import binary_value
from HW2_2018051 import prime_implicants_call
from HW2_2018051 import prime_implicants
from HW2_2018051 import groups
from HW2_2018051 import simplification
from HW2_2018051 import necessary_implicants


class testpoint(unittest.TestCase):
	def test_minFunc(self):
		self.assertEqual(minFunc(4,'(0,2,5,6,8,11) d (4,9,13)'), "w'z'+wx'z+x'y'z'+w'xy'")
		self.assertEqual(minFunc(3,'(0,2,4,7) d (3,6)'), "x+wy'+w")
		self.assertEqual(minFunc(3,'(0,1,2,3,5,7) d -'), "w'+y")
		self.assertEqual(minFunc(2, '(0,3) d (1)'), "w'+x")
		self.assertEqual(minFunc(2, '(0,1,2) d -'), "w'+x'")
                
if __name__=='__main__':
	unittest.main()
