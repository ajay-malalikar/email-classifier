from nbutils import Model


def main():
    fs = open("nbmodel.txt", "r", encoding="latin1")
    model = Model(json_data=fs.read())
    fs.close()

    print(model.vocabulary_size)
    print(model.total_ham_words)
    print(model.total_spam_words)
    print(model.spam_file_count)
    print(model.ham_file_count)


if __name__ == "__main__":
    main()