# bookbot 
# boot.dev guided project
# author: lucy

from stats import *

def main():
    path_to_file = "books/frankenstein.txt"
    file_contents = get_text(path_to_file)
    num_words = wordcount(file_contents)
    char_list = charcount(file_contents)
    sorted_chars = sorted(
        [(char, count) for char, count in char_list if char.isalpha()], 
        key=lambda pair: pair[1],
        reverse=True)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_file}...")
    print("----------- Word Count ----------")
    print(f"{num_words} words found in the document")
    print("--------- Character Count -------")
    print("")
    for char, count in sorted_chars:
        print(f"The '{char}' character was found {count} times")
    print("============= END ===============")

def get_text(filepath):
    with open(filepath) as f:
        return f.read()




if __name__ == "__main__":
    main()
