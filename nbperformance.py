from nbutils import PerformanceModel, get_model


def calculate_performance():
    model = get_model("nbperformancedata.json", PerformanceModel)
    precision_spam = model.correct_spam_files_count / model.classified_as_spam
    precision_ham = model.correct_ham_files_count / model.classified_as_ham
    recall_spam = model.correct_spam_files_count / model.spam_files_count
    recall_ham = model.correct_ham_files_count / model.ham_files_count

    print("Precision(spam): " + str(precision_spam))
    print("Recall(spam): " + str(recall_spam))
    print("F1(spam): " + str((2 * precision_spam * recall_spam) / (precision_spam + recall_spam)))
    print("Precision(ham): " + str(precision_ham))
    print("Recall(ham): " + str(recall_ham))
    print("F1(ham): " + str((2 * precision_ham * recall_ham) / (precision_ham + recall_ham)))


if __name__ == "__main__":
    calculate_performance()