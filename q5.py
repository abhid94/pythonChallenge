import urllib.request
import pickle

data = urllib.request.urlopen('http://www.pythonchallenge.com/pc/def/banner.p')
x = pickle.load(data)

counter = 1
for line in x:
    print("".join([k * v for k, v in line]))
