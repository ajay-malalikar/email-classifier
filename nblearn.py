#!/usr/bin/env python3

import os
import sys
from enum import Enum
from nbutils import Model
import json


class Category(Enum):
    spam = 1
    ham = 2

vocab_dict = {}
punctuations = {":": True, ".": True, ";": True, "-": True, "_": True, "|": True, ",": True}


def build_vocab(file, category):
    count = 0
    fs = open(file, "r", encoding="latin1")
    data = fs.readline()
    while data:
        split_words = data.strip().split()
        for w in split_words:
            if w not in punctuations:
                count += 1
                if w in vocab_dict:
                    if category is Category.spam:
                        vocab_dict[w]['spam_count'] += 1
                    else:
                        vocab_dict[w]['ham_count'] += 1
                else:
                    vocab_dict[w] = {'spam_count': 0, 'ham_count': 0}
                    if category is Category.spam:
                        vocab_dict[w]['spam_count'] += 1
                    else:
                        vocab_dict[w]['ham_count'] += 1
        data = fs.readline()
    fs.close()
    return count


def main(path):
    total_spam_words = 0
    total_ham_words = 0
    spam_file_count = 0
    ham_file_count = 0
    for root, subdir, files in os.walk(path):
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

    obj = Model(vocab_dict, total_spam_words, total_ham_words, spam_file_count, ham_file_count, len(vocab_dict))
    json_data = json.dumps(vars(obj))
    fs = open("nbmodel.txt", "w")
    fs.write(json_data)
    fs.close()

    print("Vocabulary Size: " + str(len(vocab_dict)))
    print("Total words in ham: " + str(total_ham_words))
    print("Total words in spam: " + str(total_spam_words))
    print("Spam file count: " + str(spam_file_count))
    print("Ham file count: " + str(ham_file_count))

if __name__=="__main__":
    main(sys.argv[1])

