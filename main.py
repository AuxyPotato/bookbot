# bookbot 
# boot.dev guided project
# author: lucy

from stats import wordcount, charcount

def main():
    path_to_file = "books/frankenstein.txt"
    file_contents = get_text(path_to_file)
    num_words = wordcount(file_contents)
    char_list = charcount(file_contents)
    sorted_chars = sorted(
        [(char, count) for char, count in char_list if char.isalpha()], 
        key=lambda pair: pair[1],
        reverse=True)
    print(f"--- Begin report of {path_to_file} ---")
    print(f"{num_words} words found in the document")
    print("")
    for char, count in sorted_chars:
        print(f"The '{char}' character was found {count} times")

def get_text(filepath):
    with open(filepath) as f:
        return f.read()




if __name__ == "__main__":
    main()
