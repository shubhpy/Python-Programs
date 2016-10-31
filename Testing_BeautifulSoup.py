from bs4 import BeautifulSoup
import urllib2
import tempfile

# url='http://www.azlyrics.com/lyrics/samsmith/staywithme.html'
# url="http://www.azlyrics.com/lyrics/samsmith/imnottheonlyone.html"
# conn = urllib2.urlopen(url,timeout=20)
# content=conn.read()
# fin = open("Testting_BeautifulSoup.html","w")
# fin.write(content)

with open('Testting_BeautifulSoup.html', 'r') as content_file:
	content = content_file.read()

soup = BeautifulSoup(content)

mydivs = soup.findAll("div", { "class" : "col-xs-12 col-lg-8 text-center" })

# strting=str(mydivs[0])
# soup2 = BeautifulSoup(strting)
# mydivs2= soup2.findAll("div",{"class":None})
# for A_string in mydivs2[0].strings:
# 	if A_string!="\n":
# 		if A_string.find("Verse")==-1 and A_string.find("Chorus")==-1:
# 			print A_string,
# 		# elif A_string.find("Verse")!=-1 or A_string.find("Chorus")!=-1:
# 		# 	print "\r",
# 	else:
# 		print "\n",


for div_None in mydivs:
	mydivs2= div_None.find_all("div",{"class":None})
	hi=1
	for A in mydivs2:
		Lyrics=""
		count=0
		for A_string in A:
			if A_string!="\n":
				count+=1
				if A_string.find("Verse")==-1 and A_string.find("Chorus")==-1 and count>=2:
					Lyrics+=A_string
				# else:
			else:
				Lyrics+="\n"
print Lyrics

# url="http://search.azlyrics.com/search.php?q=stay+with+me+sam+smith"
# conn = urllib2.urlopen(url,timeout=20)
# content=conn.read()
# fin = open("Testting_BeautifulSoup2.html","w")
# fin.write(content)

temp = tempfile.TemporaryFile()
with open('Testting_BeautifulSoup.html', 'r') as content_file:
	temp.write(content_file.read())
# url="http://search.azlyrics.com/search.php?q=all+of+me+john+legend"
# conn = urllib2.urlopen(url,timeout=20)
# content=conn.read()

with open("temp", 'r') as content_file:
	content = content_file.read()

soup = BeautifulSoup(content)
mydivs = soup.findAll("td", { "class" : "text-left visitedlyr" })
for tr in mydivs:
	ALLb=tr.find_all("b")
	print tr.a["href"],ALLb[0].string +" by "+ALLb[1].string