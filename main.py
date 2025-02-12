# bookbot 
# author: lucy

from collections import Counter

path_to_file = "books/frankenstein.txt"

def main():
    with open(path_to_file) as f:
        file_contents = f.read()
        print(file_contents)

def wordcount():
    with open(path_to_file) as f:
        file_contents = f.read()
        return(len(file_contents.split()))

def charcount():
    with open(path_to_file) as f:
        file_contents = f.read()
        contents_lowercase = file_contents.lower()
        charcount = Counter(contents_lowercase)
        return(charcount)


charcount()


def report():
    print(f"--- Begin report of {path_to_file} ---")
    print(f"{wordcount()} words found in the document")
    print("")
    






if __name__ == "__main__":
    main()

report()