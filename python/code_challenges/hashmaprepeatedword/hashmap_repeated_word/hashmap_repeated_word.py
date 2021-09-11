import re

words_pattern = "[a-zA-Z]+"


def repeated_word(string: str) -> str:
    array_of_words = re.findall(words_pattern, string, flags=re.IGNORECASE)
    dic = {}
    for word in array_of_words:
        if word in dic:
            return word

        else:
            dic[word] = 0


string = "this is a a test, and is this  also for the argument "
first_repeated_word = repeated_word(string)
print(first_repeated_word)
