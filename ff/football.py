import urllib2
fball = "http://www.espn.com/fantasy/football/story/_/id/15592938/eric-karabell-top-100-rankings-2016-fantasy-football-nfl"

page = urllib2.urlopen(fball)

#print "hello football"

from bs4 import BeautifulSoup
soup = BeautifulSoup(page, "lxml")

# print soup.prettify()

print soup.title

#print soup.title.string

#print soup.a

#print "***"

#all_links=soup.find_all("a")
# for link in all_links:
# 	print link.get("href")


all_tables=soup.find_all('table', class_='inline-table')
# print all_tables

table_wr=all_tables[1]
#print table_wr

rank=[]
team=[]
position=[]

for row in table_wr.findAll("tr"):
	cells = row.findAll('td')
    	if len(cells) == 3:
    		rank.append(cells[0])
    		team.append(cells[1].find(text=True))
    		position.append(cells[2].find(text=True))

# print rank
# print team
# print position

#import pandas to convert list to data frame
import pandas as pd
df=pd.DataFrame(rank,columns=['rank/player'])
df['team']=team
df['position']=position
df



print df
