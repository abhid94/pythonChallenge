#Used to make requests
import urllib.request
import re

'''
x = urllib.request.urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345')
data = x.read().decode('utf-8')
print(data)
num = re.findall('\d+', data)


url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
url = url + str(num[0])
print(url)

z = urllib.request.urlopen(url)
data2 = z.read().decode('utf-8')
print(data2)

'''

#loop the above logic
url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
num = ['12345']
pattern = re.compile("and the next nothing is (\d+)")

while True :
    x = urllib.request.urlopen(url + str(num))
    data = x.read().decode('utf-8')
    print(data)
    match = pattern.search(data)
    if match == None :
        break;
    num = match.group(1)

print("reached the end")
