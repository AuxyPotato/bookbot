# bookbot 
# boot.dev guided project
# a small program that calculates the amount of characters and words in a book
# author: lucy

from stats import wordcount, charcount, sort_characters

def main():
    path_to_file = "books/frankenstein.txt"
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
    print(f"{num_words} words found in the document")
    print("--------- Character Count -------")
    print("")
    for char, count in sorted_chars:
        print(f"The '{char}' character was found {count} times")
    print("============= END ===============")


if __name__ == "__main__":
    main()
