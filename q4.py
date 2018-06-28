#Used to make requests
import urllib.request
import re

x = urllib.request.urlopen('http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=12345')
data = x.read().decode('utf-8')
print(data)
num = re.findall('\d+', data)

url = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing="
url = url + str(num[0])
print(url)

#loop the above logic 
#while True :
