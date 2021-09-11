from python.code_challenges.hashtable.hashtable.hash_table import Hashtable


def left_join(ht1, ht2):
    intersection_output = []
    for i in ht1.array:
        if i:
            intersection = []
            current_value = i.head
            while current_value:
                intersection.append(current_value.value[0])
                intersection.append(current_value.value[1])
                if ht2.contains(current_value.value[0]):
                    intersection.append(ht2.get(current_value.value[0]))
                else:
                    intersection.append(None)
                current_value = current_value.next

            intersection_output.append(intersection)
    return intersection_output


# import re
# words_pattern = '[a-zA-Z]+'


# def repeated_word(string: str) -> str:
#     array_of_words = re.findall(words_pattern, string, flags=re.IGNORECASE)
#     dic = {}
#     for word in array_of_words:
#         if word in dic:
#             return word

#         else:
#             dic[word] = 0


# string = 'this is a a test, and is this  also for the argument '
# first_repeated_word = repeated_word(string)
# print(first_repeated_word)
