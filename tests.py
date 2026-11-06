import unittest
from check_pwd import check_pwd

"""
Must be between 8 and 20 characters (inclusive)
Must contain at least one lowercase letter (standard English alphabet)
Must contain at least one uppercase letter (standard English alphabet)
Must contain at least one digit
Must contain at least one symbol from: ~`!@#$%^&*()_+-= 
(copy and paste to avoid missing characters) These are the only symbols that will meet this requirement. 
Other symbols may be present, but they won't satisfy this requirement.
"""

class TestCheckPassword(unittest.TestCase):
    def test1(self):
        input = ""
        expected = False
        self.assertEqual(check_pwd(input), expected)

    def test2(self):
        input = "a"
        expected = False
        self.assertEqual(check_pwd(input), expected)

    def test3(self):
        input = "aaaaaaaa"
        expected = False
        self.assertEqual(check_pwd(input), expected)

if __name__ == '__main__':
    unittest.main()
