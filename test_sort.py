import pytest
from insertion_sort import insertion_sort




@pytest.fixture(scope="function")
def build_list():
    unsort = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    sort = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    unsort_repeated = [10, 9, 10, 9, 10, 9, 10, 9, 10, 9]
    sorted_repeated = [9, 9, 9, 9, 9, 10, 10, 10, 10, 10]
    return unsort, sort, unsort_repeated, sorted_repeated

def test_insertion(build_list):
    x, y, a, b = build_list
    assert insertion_sort(x) == y
    assert insertion_sort(a) == b