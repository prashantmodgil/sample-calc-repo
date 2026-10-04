import pytest
from calc import add, process_map

def test_add():
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
    assert add(-1, -1) == -2
def test_process_map():
    map = {'a': 1, 'b': 2, 'c': 3}
    assert process_map(map) == [1, 2, 3]

