import unittest

import sys
sys.path.append('..')
from translator import english_to_french, french_to_english

class TestE2F(unittest.TestCase):
    def test1(self):
        self.assertEqual(english_to_french('Hello'), 'Bonjour')
        self.assertNotEqual(english_to_french('Hello'), 'Aloha')

class TestF2e(unittest.TestCase):
    def test2(self):
        self.assertEqual(french_to_english('Bonjour'), 'Hello')
        self.assertNotEqual(french_to_english('Hello'), 'Konnichiwa')

unittest.main()
