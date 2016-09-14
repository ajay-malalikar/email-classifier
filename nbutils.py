import json
from enum import Enum


class Model:
    """
        Model for serialization and deserialization of learnt data
    """
    def __init__(self, vocab=None, total_spam_words=0, total_ham_words=0, spam_file_count=0,
                 ham_file_count=0, vocabulary_size=0, json_data=None):
        if json_data is None:
            self.vocab_dict = vocab
            self.total_spam_words = total_spam_words
            self.total_ham_words = total_ham_words
            self.spam_file_count = spam_file_count
            self.ham_file_count = ham_file_count
            self.vocabulary_size = vocabulary_size
        else:
            self.__dict__ = json.loads(json_data)


class PerformanceModel:
    """
        Model for serialization and deserialization of performance parameters
    """
    def __init__(self, spam_files_count=0, ham_files_count=0, correct_spam_files_count=0, correct_ham_files_count=0,
                 classified_as_spam=0, classified_as_ham=0, json_data=None):
        if json_data is None:
            self.spam_files_count = spam_files_count
            self.ham_files_count = ham_files_count
            self.correct_spam_files_count = correct_spam_files_count
            self.correct_ham_files_count = correct_ham_files_count
            self.classified_as_spam = classified_as_spam
            self.classified_as_ham = classified_as_ham
        else:
            self.__dict__ = json.loads(json_data)


class Category(Enum):
    """
    Enum for classes spam and ham
    """
    spam = 1
    ham = 2


def get_model(file, model_class):
    fs = open(file, "r", encoding="latin1")
    model = model_class(json_data=fs.read())
    fs.close()
    return model
