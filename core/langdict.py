from collections import UserDict
import csv
import re

from .clean_csv import cleanFunc

# combine csvs into one csv?

class LangDict(UserDict):
    # creates a LangDict object from a csv file

    @classmethod
    def from_csv(cls,path):
        # ['word and its def'] --> {'word': ['and', 'its', 'def']}
        dict_as_list = cleanFunc(path)
        #transform list of strings into list of lists
        temp = [string.split(' ') for string in dict_as_list]

        #transform list of lists into dict where the first
        #word in each list is the key
        from_csv_dict = {}
        for i in temp:
            #checks for mutilpe definitions
            if i[0] in from_csv_dict:
                from_csv_dict[i[0]] += i[1:]
            else:
                from_csv_dict[i[0]] = i[1:]

        from_csv_dict = LangDict(from_csv_dict)

        return from_csv_dict

    def add(self,dict_2):
        """if isinstance(self, LangDict) and isinstance(dict_2, Langdict):"""
        return {**self, **dict_2}
