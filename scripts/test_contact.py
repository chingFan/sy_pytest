import pytest


class TestPytest:

    def test_pytest1(self):
        print("1")
        assert 1

    def test_pytest2(self):
        print("0")
        assert 1

    def test_pytest3(self):
        print("0")
        assert 1

    def test_pytest4(self):
        print("0")
        assert 0

