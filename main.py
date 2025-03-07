# BookBot is a Boot.dev guided project.
#
# It takes a text file as input by running the program as 'python 3 main.py /path/to/file'.
# The program will calculate the amount of words and characters in the file. It will also
# generate a list of of each character in order of occurrence, listing the amounts of each.

import sys

from stats import wordcount, charcount, sort_characters

def main():
    path_to_file = filepath()
    file_contents = get_text(path_to_file)
    num_words = wordcount(file_contents)
    char_list = charcount(file_contents)
    sorted_chars = sort_characters(char_list)
    generate_report(path_to_file, num_words, sorted_chars)

def get_text(filepath):
    with open(filepath) as f:
        return f.read()

def generate_report(path_to_file, num_words, sorted_chars):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    print("")
    for char, count in sorted_chars:
        print(f"{char}: {count}")
    print("============= END ===============")

def filepath():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        return sys.argv[1]


if __name__ == "__main__":
    main()
