# 66831

import urllib2
import re

num = 37278
i = 0
while(i <= 401):
    response = urllib2.Request(url = 'http://www.pythonchallenge.com/pc/def/linkedlist.php?nothing='+str(num))
    f = urllib2.urlopen(response)
    text = f.read()
    nothings = re.findall(r'\d+', text)
    num = str(nothings[0])
    print i, num
    i+=1
