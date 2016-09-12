#!/usr/bin/env python3

import os
from enum import Enum


class Category(Enum):
    spam = 1
    ham = 2

spam_dict = dict()
ham_dict = dict()
punctuations = {":": True, ".": True, ";": True, "-": True, "_": True, "|": True, ",": True}


def build_vocab(file, category):
    dictionary = spam_dict if category is Category.spam else ham_dict
    count = 0
    fs = open(file, "r", encoding="latin1")
    data = fs.readline()
    while data:
        split_words = data.strip().split()
        for w in split_words:
            if w not in punctuations:
                count += 1
                if w in dictionary:
                    dictionary[w] += 1
                else:
                    dictionary[w] = 1
        data = fs.readline()
    return count



def main():
    total_spam_words = 0
    total_ham_words = 0
    spam_file_count = 0
    ham_file_count = 0
    for root, subdir, files in os.walk("train"):
        if len(files) is not 0:
            for file in files:
                if 'ham' in root:
                    ham_file_count += 1
                    total_ham_words += build_vocab(root+"/" + file, Category.ham)
                elif 'spam' in root:
                    spam_file_count += 1
                    total_spam_words += build_vocab(root + "/" + file, Category.spam)
                else:
                    pass
    print("Unique words in spam: " + str(len(spam_dict)))
    print("Unique words in ham: " + str(len(ham_dict)))
    print("Vocabulary Size: " + str(len(spam_dict) + len(ham_dict)))
    print("Total words in ham: " + str(total_ham_words))
    print("Total words in spam: " + str(total_spam_words))
    print("Spam file count: " + str(spam_file_count))
    print("Ham file count: " + str(ham_file_count))


if __name__=="__main__":
    main()

