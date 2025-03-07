# BookBot is a Boot.dev guided project.
#
# This stats file takes the file contents retrieved in main.py and
# runs the calculations on them. These functions are imported in main.py
# and called there to practice inter-file operations.

from collections import Counter

def wordcount(file_contents):
    """This returns the amount of words in the file."""
    return len(file_contents.split())

def charcount(file_contents):
    """This returns the amount of characters, converted to lowercase."""
    return list(Counter(file_contents.lower()).items())

def sort_characters(char_list):
    """This sorts all alpha characters into a list with counts."""
    return sorted(
        [(char, count) for char, count in char_list if char.isalpha()], 
        key=lambda pair: pair[1],
        reverse=True)
