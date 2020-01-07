import unittest
import os
import types
import re

from ..clean_csv import cleanFunc

#Pre process the CSVfile
class Test_cleanFunc(unittest.TestCase):

    csv_path = '/Users/peterwalker/Desktop/projects/langdict/core/data/Dictionary_in_csv/X.csv'
    clean_list = cleanFunc(csv_path)

    def test_csv_clean(self):
        for string in self.clean_list:
            #all lowercase and spaces
            self.assertNotRegex(string, r'[^a-z ]')

            #deleted all empty lines ie \n
            self.assertEqual(len(self.clean_list), 147)
