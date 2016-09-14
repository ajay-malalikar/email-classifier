import sys
import os
import math
import json
import timeit
from nbutils import Model, Category, PerformanceModel, get_model


def classify(file, model):
    fs = open(file, "r", encoding="latin1")
    data = fs.read().strip().split()
    p_spam = math.log(model.spam_file_count / (model.ham_file_count + model.spam_file_count))
    p_ham = math.log(model.ham_file_count / (model.ham_file_count + model.spam_file_count))
    try:
        for d in data:
            if d in model.vocab_dict:
                p_spam += math.log((model.vocab_dict[d]['spam_count']+1) / (model.total_spam_words+model.vocabulary_size))
                p_ham += math.log((model.vocab_dict[d]['ham_count']+1) / (model.total_ham_words+model.vocabulary_size))
    except:
        print(sys.exc_info()[0])
    fs.close()
    if p_spam < p_ham:
        return Category.ham
    else:
        return Category.spam


def main(path):
    output = {}
    spam_files_count = 0
    ham_files_count = 0
    correct_spam_files_count = 0
    correct_ham_files_count = 0
    classified_as_spam = 0
    classified_as_ham = 0
    model = get_model("nbmodel.txt", Model)
    for root, subdir, files in os.walk(path):
        for file in files:
            category = classify(root + "/" + file, model)
            if "spam" in root:
                spam_files_count += 1
                if category is Category.spam:
                    classified_as_spam += 1
                    correct_spam_files_count += 1
                    output[root + "/" + file] = "spam"
                else:
                    classified_as_ham += 1
                    output[root + "/" + file] = "ham"
            elif "ham" in root:
                ham_files_count += 1
                if category is Category.ham:
                    classified_as_ham += 1
                    correct_ham_files_count += 1
                    output[root + "/" + file] = "ham"
                else:
                    classified_as_spam += 1
                    output[root + "/" + file] = "spam"
            else:
                pass

    performance_model = PerformanceModel(spam_files_count, ham_files_count, correct_spam_files_count,
                                         correct_ham_files_count, classified_as_spam, classified_as_ham)
    # Delete if the file is already present
    try:
        os.remove("nbperformancedata.json")
    except OSError:
        pass
    fs = open("nbperformancedata.json", "w")
    fs.write(json.dumps(vars(performance_model)))
    fs.close()

    # Delete if the file is already present
    try:
        os.remove("nboutput.txt")
    except OSError:
        pass

    fs = open("nboutput.txt", "a")
    for k, v in output.items():
        fs.write(v + " " + k + '\n')
    fs.close()

if __name__ == "__main__":
    start=timeit.default_timer()
    main(sys.argv[1])
    stop = timeit.default_timer()
    print(stop-start)