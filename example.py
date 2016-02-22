import unittest
import exampleCode

class TestStringMethods(unittest.TestCase):
	
	def test_upper(self):
		self.assertEqual(exampleCode.toUpper('foo'), 'FOO')
		
	def test_isupper(self):
		self.assertTrue(exampleCode.testUpper('FOO'))
		self.assertFalse(exampleCode.testUpper('Foo'))
	
	def test_split(self):
		s = 'hello world'
		self.assertEqual(exampleCode.stringSplit(s), ['hello', 'world'])
		
if __name__ == '__main__':
    unittest.main()
