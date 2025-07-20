import sys

from stats import count_characters_in_text, count_words_in_text, dict_to_sorted_dictlist


def get_book_content(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    # print(file_contents)
    return file_contents


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]
    content = get_book_content(filepath)

    num_words = count_words_in_text(content)

    dict_character_count = count_characters_in_text(content)
    sorted_char_count = dict_to_sorted_dictlist(dict_character_count)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for entry in sorted_char_count:
        print(f"{entry["char"]}: {entry["num"]}")

    print("============= END ===============")


main()
