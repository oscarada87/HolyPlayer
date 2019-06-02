from unittest import TestCase
import pytest


class ExampleTest(TestCase):
    """這裡教你怎麼寫出厲害的 Test Case！"""

    def setUp(self):
        """測試前先建立好環境"""
        self.data1 = 87
        self.data2 = "Holy Player"

    def tearDown(self):
        """測試結束後收拾環境"""
        pass

    def test_example(self):
        """測試測起來"""
        self.assertEqual(88, self.data1 + 1)
        self.assertEqual("Holy Player!", self.data2 + "!")