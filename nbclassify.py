import sys
import os
import math
import timeit
from nbutils import Model, Category, get_model


def classify(file, model):
    fs = open(file, "r", encoding="latin1")
    data = fs.read().strip().split()
    p_spam = math.log(model.spam_file_count / (model.ham_file_count + model.spam_file_count))
    p_ham = math.log(model.ham_file_count / (model.ham_file_count + model.spam_file_count))
    try:
        for d in data:
            if d in model.vocab_dict:
                p_spam += math.log((model.vocab_dict[d]['s']+1)) - math.log((model.total_spam_words+model.vocabulary_size))
                p_ham += math.log((model.vocab_dict[d]['h']+1)) - math.log((model.total_ham_words+model.vocabulary_size))
    except:
        print(sys.exc_info()[0])
    fs.close()
    if p_spam < p_ham:
        return Category.ham
    else:
        return Category.spam


def main(path):
    output = {}
    model = get_model("nbmodel.txt", Model)
    for root, subdir, files in os.walk(path):
        for file in files:
            category = classify(root + "/" + file, model)
            output[root + "/" + file] = "spam" if category is Category.spam else "ham"
    fs = open("nboutput.txt", "a")
    for k, v in output.items():
        fs.write(v + " " + k + '\n')
    fs.close()

if __name__ == "__main__":
    start = timeit.default_timer()
    main(sys.argv[1])
    stop = timeit.default_timer()
    print(stop-start)
