import os
import sys
import json
import timeit
from nbutils import Model, Category

vocab_dict = {}


def build_vocab(file, category):
    count = 0
    fs = open(file, "r", encoding="latin1")
    for data in fs:
        split_words = data.strip().split()
        for w in split_words:
            count += 1
            if w in vocab_dict:
                if category is Category.spam:
                    vocab_dict[w]['s'] += 1
                else:
                    vocab_dict[w]['h'] += 1
            else:
                vocab_dict[w] = {'s': 0, 'h': 0}
                if category is Category.spam:
                    vocab_dict[w]['s'] += 1
                else:
                    vocab_dict[w]['h'] += 1
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

    with open("nbmodel.txt", "w") as fs:
        fs.write(json_data)

if __name__ == "__main__":
    start=timeit.default_timer()
    main(sys.argv[1])
    stop=timeit.default_timer()
    print(str(stop-start))
