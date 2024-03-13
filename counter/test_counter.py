"""Write a unit test to verify that Counter is a singleton.

   Also verify that all instances share the same count
   and that the count is not reset to 0 when you invoke 
   count = Counter() 
   after the first time.

   You can use pytest or unittest.
"""
import unittest
from counter import Counter


class TestCounter(unittest.TestCase):
    def test_same_object(self):
        counter = Counter()
        counter2 = Counter()
        self.assertIs(counter, counter2)
        counter3 = Counter()
        self.assertIs(counter, counter2, counter3)

    def test_does_not_reset(self):
        counter = Counter()
        counter.increment()
        counter2 = Counter()
        self.assertEqual(1, counter.count)
        self.assertEqual(1, counter2.count)

    def test_share_same_count(self):
        counter = Counter()
        counter2 = Counter()
        counter.increment()
        self.assertEqual(counter.count, counter2.count)
        counter2.increment()
        self.assertEqual(counter.count, counter2.count)