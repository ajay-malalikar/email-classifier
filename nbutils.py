import json
from enum import Enum

"""
Model for serialization and deserialization of learnt data
"""
class Model():
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

"""
Enum for classes spam and ham
"""
class Category(Enum):
    spam = 1
    ham = 2

"""
Code to generate 10% training data
"""