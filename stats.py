# bookbot
# statistics calculation
# author: lucy


from collections import Counter

def wordcount(file_contents):
    return(len(file_contents.split()))

def charcount(file_contents):
    return(list(Counter(file_contents.lower()).items()))
    