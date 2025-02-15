# bookbot 
# boot.dev guided project
# author: lucy

from collections import Counter

def main():
    path_to_file = "books/frankenstein.txt"
    file_contents = get_text(path_to_file)
    num_words = wordcount(file_contents)
    num_chars = charcount(file_contents)
    print(f"--- Begin report of {path_to_file} ---")
    print(f"{num_words} words found in the document")
    print(num_chars)


def wordcount(file_contents):
    return(len(file_contents.split()))

def charcount(file_contents):
    return(Counter(file_contents.lower()))

def get_text(path):
    with open(path) as f:
        return f.read()




if __name__ == "__main__":
    main()
