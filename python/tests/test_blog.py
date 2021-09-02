from code_challenges.blog.blog import __version__
from code_challenges.blog.blog.insertion_sort import insertionSort


def test_version():
    assert __version__ == '0.1.0'


def test_insortion():
    arr = [5, 4, 3, 7]
    new_arr = insertionSort(arr)

    actual = [3, 4, 5, 7]
    excepted = new_arr

    assert actual == excepted
