from unittest import TestCase
import pytest

# 測試用 Class 寫法
# 暫時跳過
@pytest.mark.skipif()
class TestExample01(TestCase):
    # 執行每個函數前會先執行這個
    def setUp(self):
        self.data1 = 87
        self.data2 = "Holy Player"

    # 執行結束後會執行這個
    def tearDown(self):
        pass

    def test_example(self):
        self.assertEqual(88, self.data1 + 1)
        self.assertEqual("Holy Player!", self.data2 + "!")