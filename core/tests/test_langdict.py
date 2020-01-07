import unittest
import os
import re

from ..langdict import LangDict

class Test_lang_dict(unittest.TestCase):
    #simple test case dict
    letters = {'a':['c','e','g'],
            'b':['a','d','c','e','f','g',],
            'c':['a','d','g','h'],
            'd':['d','c','f','g'],
            'e':['d','g'],
            'f':['j'],
            'g':['h'],
            'h':['a','e','g'],
            'j':['a','g'],
            'k':['e','f','g']
            }

    #X.csv as test case
    csv_path = '/Users/peterwalker/Desktop/projects/langdict/core/data/Dictionary_in_csv/X.csv'
    #Y.csv as test case
    csv_path_2 = '/Users/peterwalker/Desktop/projects/langdict/core/data/Dictionary_in_csv/Y.csv'


    test_dict_X = LangDict.from_csv(csv_path)
    test_dict_Y = LangDict.from_csv(csv_path_2)

    def test_instantiate(self):
        #simple case
        self.assertIsInstance(LangDict(self.letters),LangDict)
        #x.csv case
        self.assertIsInstance(self.test_dict_X, LangDict)

    def test_retrieve_val(self):
        self.assertTrue(self.test_dict_X['xanthelasma'] == ['see', 'xanthoma'])
        self.assertTrue(self.test_dict_X['xiphosura'] == ['see', 'xiphura'])

    def test_add_dicts(self):
        test_dict_XY = self.test_dict_X.add(self.test_dict_Y)
        # test proper combination of graphs
        self.assertTrue(test_dict_XY['xanthelasma'] == ['see', 'xanthoma'])
        self.assertTrue(test_dict_XY['ya'] == ['yea'])

    def test_combine_multiple_defs(self):
        '''Xanthogen (n.) The hypothetical radical supposed to be characteristic of xanthic acid.

        Xanthogen (n.) Persulphocyanogen.

        words with multiple definitions are combined, Xanthogen is the 18th
        unique word in X.csv
        '''
        self.assertTrue(self.test_dict_X['xanthogen'] == ['the', 'hypothetical', 'radical', 'supposed', 'to', 'be', 'characteristic', 'of', 'xanthic', 'acid', 'persulphocyanogen'])

    def test_to_pickle(self):
        self.assertTrue(False)

    def test_from_pickle(self):
        self.assertTrue(False)
