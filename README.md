## Parser from text file into CSV format.

Requirements: </br>
```bash
pip3 intall -r requirements.txt
```

Usage: </br>
```bash
python3 parser.py <input_file> <optional soutput_file>
```

Tokenizer is adjusted to handle lines in form:

`[string without numbers][1 or more numbers in form <2 or 3  digits>.<2 digits>]`

Sample text: "Antropozoologia57.28Archaeology41.0070.64Archeologia30.8264.44Architektura przestrzeni informacyjnych43.2950.60"

Firstly tokenizer splits text into lines using line_regex, next each line is tokenized using token_regex. It is also possible to adjust CSV column deliminiter using column_deliminiter virable as well as line deliminiter through line_deliminiter virable.

Configuring virables parser:</br>
```python
column_deliminiter = '^' 
line_deliminiter = '\n'
header = f"Kierunek{column_deliminiter}Prog 1{column_deliminiter}Prog 2{column_deliminiter}Prog 3\n"
line_regex = r'\D+(?:\d{2,3}.\d{2}\*{0,1})+' #pattern for line
token_regex = r'(?!\.)\D+|\d{2,3}.\d{2}\*{0,1}' #pattern for token
 ``` 