import sys
import os
import math
from nbutils import Model, Category

model = None
pSpam = None
pHam = None

def get_model():
    fs = open("nbmodel.txt", "r", encoding="latin1")
    global model
    model = Model(json_data=fs.read())
    global pSpam
    pSpam = model.spam_file_count / (model.ham_file_count + model.spam_file_count)
    global pHam
    pHam = model.ham_file_count / (model.ham_file_count + model.spam_file_count)
    fs.close()


def classify(file):
    fs = open(file, "r", encoding="latin1")
    data = fs.read().strip().split()
    p_spam = math.log(pSpam)
    p_ham = math.log(pHam)
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
    matcher = {"spam": 0, "ham": 0}
    spam_files_count = 0
    ham_files_count = 0
    get_model()
    for root, subdir, files in os.walk(path):
        for file in files:
            category = classify(root + "/" + file)
            if "spam" in root:
                spam_files_count += 1
                if category is Category.spam:
                    matcher["spam"] += 1
            elif "ham" in root:
                ham_files_count += 1
                if category is Category.ham:
                    matcher["ham"] += 1
            else:
                pass

    print("Total spam files: " + str(spam_files_count))
    print("Correct match: " + str(matcher["spam"]))
    print("Total ham files: " + str(ham_files_count))
    print("Correct match: " + str(matcher["ham"]))

if __name__ == "__main__":
    main(sys.argv[1])