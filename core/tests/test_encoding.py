import os
import unittest

directory = '/Users/peterwalker/Desktop/projects/langdict/core/data/Dictionary_in_csv/'

class Test_encoding(unittest.TestCase):

    def test_encoding(self):

        for file in os.listdir(directory):
            with open(directory + file, 'rb') as f:
                for i, line in enumerate(f, 1):
                    try:
                        line.decode('utf-8')
                    except UnicodeDecodeError as e:
                        print('File: {}, Line: {}, Offset:{}, {}'.format(file, i, e.start, e.reason))
