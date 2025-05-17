import unittest

class TestRecetas(unittest.TestCase):
    def test_dummy(self):
        self.assertEqual(2 + 2, 4)

    def test_always_pass(self):
        self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()