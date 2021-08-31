from mergesort import __version__
from mergesort.merge_sort import mergeSort


def test_version():
    assert __version__ == '0.1.0'


def test_merge_sort():
    arr = [5, 4, 3, 7]
    new_arr = mergeSort(arr)

    actual = [3, 4, 5, 7]
    excepted = new_arr

    assert actual == excepted
