from stats import get_num_words, get_num_chars, get_num_chars_report
import sys


def get_book_text(file_path):
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    file_path = sys.argv[1]

    file_contents = get_book_text(file_path)
    count = get_num_words(file_contents)
    chars_dict = get_num_chars(file_contents)
    alpha_count = get_num_chars_report(chars_dict)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    for char_count in alpha_count:
        print(f"{char_count['char']}: {char_count['nums']}")
    print("============= END ===============")


main()
