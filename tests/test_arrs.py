import pytest

from utils import arrs


@pytest.fixture
def _list():
    return [1, 2, 3, 4]


def test_get(_list):
    assert arrs.get(_list, 1, "test") == 2
    assert arrs.get([], 0, "test") == "test"
    assert arrs.get(_list, -2, "test") == "test"


def test_slice(_list):
    assert arrs.my_slice(_list, 1, 3) == [2, 3]
    assert arrs.my_slice(_list, 1) == [2, 3]
    assert arrs.my_slice([], 1, 2) == []
    assert arrs.my_slice(_list, -4, 2) == [1, 2]
    assert arrs.my_slice([1], -3) == [1]
