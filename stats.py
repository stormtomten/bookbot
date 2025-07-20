def count_words_in_text(text):
    word_list = text.split()
    return len(word_list)


def count_characters_in_text(text):
    text = text.lower()
    char_dict = {}

    for char in text:
        if char in char_dict:
            char_dict[char] += 1
        else:
            char_dict[char] = 1
    return char_dict


def sort_on_num(item):
    return item["num"]


def dict_to_sorted_dictlist(dict):

    dict_list = []

    for key in dict:
        if key.isalpha():
            dict_list.append({"char": f"{key}", "num": dict[key]})

    dict_list.sort(reverse=True, key=sort_on_num)
    return dict_list
