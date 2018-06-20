F = open("p2Text.txt", "r");

text = F.read();

for char in '\n!@#$%^&*(){}+_[]':
    text = text.replace(char, '');

print(text)
