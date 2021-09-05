from code_challenges.hashmaprepeatedword.hashmap_repeated_word.hashmap_repeated_word import repeated_word


def test_repeated():
    string = ' hello from the other world, hello'
    actual = repeated_word(string)
    expected = 'hello'
    assert actual == expected


def test_repeated2():
    string = ' hello from the other world, hello from '
    actual = repeated_word(string)
    expected = 'from'
    assert actual != expected


def test_repeated3():
    string = ' hello from the the other world, hello'
    actual = repeated_word(string)
    expected = 'the'
    assert actual == expected
