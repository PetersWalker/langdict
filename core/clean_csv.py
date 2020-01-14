import re

def cleanFunc(path):
    #open csvfile
    with open(path, encoding='mac-roman') as file:
        #turn file into list of strings

        #unicode error in for loop for multiple csvs
        cleanable = [ str(line) for line in file ]

        #regex for all non alphabet and space characters
        alpha_regex = re.compile(r'[^a-zA-Z ]')

        #regex for parts of speech and other "in parentheses, non greedy"
        pos_regex = re.compile(r'\(.*\)')

        #regex for spaces
        spaces_regex = re.compile(r' +')

        cleaned = []
        for string in cleanable:
            if (string == '\n'):
                pass
            else:
                temp1 = pos_regex.sub('', string)
                temp2 = spaces_regex.sub(' ', temp1)
                temp3 = alpha_regex.sub('', temp2).lower()
                cleaned.append(temp3)


    # list of strings
    return cleaned
