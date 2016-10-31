from urllib import urlopen
from BeautifulSoup import BeautifulSoup
import re

webpage = urlopen ('http://www.newthinktank.com/2010/11/python-2-7-tutorial-pt-13-website-scraping/').read()

patFinderTitle = re.compile('<title>(.*)</title>')

patFinderLink = re.compile('<link rel.*href="(.*)"/>')

findPatTitle = re.findall(patFinderTitle,webpage)
findPatLink = re.findall(patFinderLink,webpage)

listItr = []

listItr[:]=range(2,5)

for i in listItr:
	print findPatTitle[i]
	print findPatLink[i]
	print "\n"