import urllib.request
import re
html = urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/ocr.html").read().decode()
data = re.findall("<!--(.*?)-->", html, re.DOTALL)[-1]
print("".join(re.findall("[A-Za-z]", data)))


html = urllib.request.urlopen("http://www.pythonchallenge.com/pc/def/equality.html").read().decode()
data = re.findall("<!--(.*)-->", html, re.DOTALL)[-1]
print("".join(re.findall("[^A-Z]+[A-Z]{3}([a-z])[A-Z]{3}[^A-Z]+", data)))

from urllib.request import urlopen

uri = "http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing=%s"

num = "12345"
#num = str(16044/2)

pattern = re.compile("and the next nothing is (\d+)")

while(True):
    content = urlopen(uri % num).read().decode('utf-8')
    print(content)
    match = pattern.search(content)
    if match == None:
        break
    num = match.group(1)

doc = urlopen("http://www.baidu.com")
print(doc.info())
print(doc.info().getheader('Content-Type'))
