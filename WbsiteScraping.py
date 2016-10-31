from urllib import urlopen
from BeautifulSoup import BeautifulSoup
import re

webpage = urlopen ('https://www.udemy.com/blog/python-sqlite/').read()

patFinderTitle = re.compile('<title>(.*)</title>')

patFinderLink = re.compile('<link rel.*href="(.*)"/>')

findPatTitle = re.findall(patFinderTitle,webpage)
findPatLink = re.findall(patFinderLink,webpage)

print findPatTitle[0]
print findPatLink[0]

listItr=[]
listItr[:]= range(0,10)

for i in listItr:
	print i
	print findPatTitle[i]
	print findPatLink[i]
	print "\n"
