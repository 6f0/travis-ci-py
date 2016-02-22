import unittest
import exampleCode

class TestStringMethods(unittest.TestCase):
	
	def test_upper(self):
		self.assertEqual(example2Code.toUpper('foo'), 'FOO')
		
	def test_isupper(self):
		self.assertTrue(example2Code.testUpper('FOO'))
		self.assertFalse(example2Code.testUpper('Foo'))
	
	def test_split(self):
		s = 'hello world'
		self.assertEqual(example2Code.stringSplit(s), ['hello', 'world'])
		
if __name__ == '__main__':
    unittest.main()
