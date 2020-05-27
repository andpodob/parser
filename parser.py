import sys
from nltk.tokenize import RegexpTokenizer

column_deliminiter = '^'
line_deliminiter = '\n'
header = f"Kierunek{column_deliminiter}Prog 1{column_deliminiter}Prog 2{column_deliminiter}Prog 3\n"
line_regex = r'\D+(?:\d{2,3}.\d{2}\*{0,1})+'
token_regex = r'(?!\.)\D+|\d{2,3}.\d{2}\*{0,1}'

def data_to_csv(datafile, outputfile="output.csv"):
    line_tokenizer = RegexpTokenizer(line_regex)
    token_tokenizer = RegexpTokenizer(token_regex)
    input_file = open(datafile, "r")
    text = input_file.read()
    lines = line_tokenizer.tokenize(text)
    output_f = open(outputfile, "w")
    output_f.write(header)
    for line in lines:
        tokens = token_tokenizer.tokenize(line)
        str = ""
        for token in tokens:
            str += token+column_deliminiter
        str = str[:-1]+line_deliminiter
        output_f.write(str)

    input_file.close()
    output_f.close()


if len(sys.argv) == 2:
    data_to_csv(sys.argv[1])
elif len(sys.argv) == 3:
    data_to_csv(sys.argv[1], sys.argv[2])
else:
    print("python3 parser.py <input_file> //optional:<output_file>")