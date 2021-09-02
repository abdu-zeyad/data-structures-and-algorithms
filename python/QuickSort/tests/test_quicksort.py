from quicksort import __version__
from quicksort.quicksort import quick_sort


def test_version():
    assert __version__ == '0.1.0'


def test_quick_sort():
    arr = [5, 4, 3, 7]
    quick_sort(0, len(arr) - 1, arr)

    actual = arr
    excepted = [3, 4, 5, 7]

    assert actual == excepted
