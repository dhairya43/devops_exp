import unittest

class TestStringMethods(unittest.TestCase):
    
    def test_positive(self):
        username = input("Please enter your username ")
        str = input("Please enter your password ")
        self.assertEqual(username,'dhairya')
        self.assertEqual(str,'@Password99')
        

if __name__ == '__main__':
    unittest.main()
