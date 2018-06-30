import re

F = open("p3Text.txt", "r");
text = F.read();
outputs = re.findall('[a-z][A-Z]{3}[a-z][A-Z]{3}[a-z]', text)


for output in outputs:
    x = re.findall('[A-Z]{1}[a-z][A-Z]{1}', output)
    for char in x:
        char = re.findall('[a-z]', char)
        print(char)
