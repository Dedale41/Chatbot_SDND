import re

def find_pages_number(sentence) :
    pattern = '([0-9]+) ?pages?'
    match = re.findall(pattern, sentence)
    if match:
        return match[0]
    return(-1)

def find_doc_name(sentence):
    # pattern = '([0-9a-zA-Z]+\.(pdf|doc|docx|odt))'
    pattern = '([0-9a-zA-Z]+\.[a-z]+)'
    match = re.findall(pattern, sentence)
    if match:
        return(match[0])
    return(-1)


if __name__ == "__main__":
    print(find_pages_number("imprime Alex de 200 pages"))