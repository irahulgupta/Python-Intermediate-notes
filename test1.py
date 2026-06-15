import unittest

def add(a, b):
    return a + b

class TestAdd(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(add(2, 3), 5)

unittest.main()