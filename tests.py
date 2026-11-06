import unittest
from check_pwd import check_pwd

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

    def test4(self):
        input = "AAAAAAAA"
        expected = False
        self.assertEqual(check_pwd(input), expected)

    def test5(self):
        input = "aaaaAAAA"
        expected = False
        self.assertEqual(check_pwd(input), expected)

    def test6(self):
        input = "aaaaAAA1"
        expected = False
        self.assertEqual(check_pwd(input), expected)

    def test7(self):
        input = "aaaaA1!@"
        expected = True
        self.assertEqual(check_pwd(input), expected)

    def test8(self):
        input = "aaaaA1!@aaaaA1!@aaaaA1!@"
        expected = False
        self.assertEqual(check_pwd(input), expected)

    def test9(self):
        input = "aaaaA1!@aaaaA1!@aaaa"
        expected = True
        self.assertEqual(check_pwd(input), expected)

    def test10(self):
        input = "aaaaA1!@aaaaA1!@aaaa!"
        expected = False
        self.assertEqual(check_pwd(input), expected)

    def test11(self):
        input = "aaaaA1!"
        expected = False
        self.assertEqual(check_pwd(input), expected)

if __name__ == '__main__':
    unittest.main()
