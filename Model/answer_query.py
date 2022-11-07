from nltk.tokenize import word_tokenize
from nltk.chunk import conlltags2tree, tree2conlltags
from nltk import pos_tag
import nltk
import re

def find_pages_number(sentence) :
    pattern = '[0-9]+ ?pages?'
    match = re.findall(pattern, sentence)
    print(match)
    if match:
        return([int(s) for s in match[0].split() if s.isdigit()])
    return(None)

def find_doc_name(sentence):
    #aled


if __name__ == "__main__":
    print(find_pages_number("imprime Alex de 200 pages"))