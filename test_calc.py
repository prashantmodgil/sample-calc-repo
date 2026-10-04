import pytest
from calc import add, process_map, bubble_sort
def test_add():
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
    assert add(-1, -1) == -2
def test_process_map():
    map = {'a': 1, 'b': 2, 'c': 3}
    assert process_map(map) == [1, 2, 3]
def test_bubble_sort():
    arr = [64, 34, 25, 12, 22, 11, 90]
    arr = bubble_sort(arr)
    assert arr == [11, 12, 22, 25, 34, 64, 90]