# bookbot
# boot.dev guided project
# statistics calculation
# author: lucy


from collections import Counter

def wordcount(file_contents):
    return(len(file_contents.split()))

def charcount(file_contents):
    return(list(Counter(file_contents.lower()).items()))

def sort_characters(char_list):
    sorted_chars = sorted(
        [(char, count) for char, count in char_list if char.isalpha()], 
        key=lambda pair: pair[1],
        reverse=True)
    return sorted_chars