import sqrteg
import unittest

class TestData(unittest.TestCase):
	TestData=( (0,0),
                   (1,1),
		   (2,4),
                   (3,9),
                   (8.5,72.25),
                   (10,100),
                   (55.55,3085.8025),
                   (100,10000) )


	def testSqItTestData(self):
		"""sqIt give known result with known output"""
		for integer,square in self.TestData:
			result=sqrteg.sqIt(integer)
			self.assertEqual(square, result)
	
	def testSqrtItTestData(self):
		"""sqrtIt give known result with known output"""
		for integer,square in self.TestData:
			result=sqrteg.sqrtIt(square)
			self.assertEqual(integer, result)



class SqItBadInput(unittest.TestCase):
	
	def testSqItInput(self):
		"""sqIt fails for bad input"""
		self.assertRaises(sqrteg.TypeError, sqrteg.sqIt, 'hello')


class SqrtItBadInput(unittest.TestCase):
	
	def testSqrtItInput(self):
		"""sqrtIt fails for bad input"""
		self.assertRaises(sqrteg.TypeError, sqrteg.sqrtIt, 'hello')
	def testNegative(self):
		self.assertRaises(sqrteg.OutOfRangeError, sqrteg.sqrtIt, -1)


class SanityCheck(unittest.TestCase): 
	
	def testSanity(self):  
		"""sqrtIt(sqIt(n))==n for all n"""
		for integer in range(1, 10000):
			square=sqrteg.sqIt(integer)
			result=sqrteg.sqrtIt(square)
			self.assertEqual(integer, result)




if __name__ == "__main__":
	unittest.main()

			

