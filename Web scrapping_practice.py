#import libraries
from bs4 import BeautifulSoup
import requests

#import csv library
import csv

#open a new csv file
file = open('scrapped_quotes.csv','w')
#create a var for writing to the csv
writer = csv.writer(file)

#create the header row of the csv
writer.writerow(['Quote','Author','Tag'])

#request webpage and store as a var
page_to_scrape = requests.get("https://quotes.toscrape.com/")
#use BS to parse the HTML and store as a var
soup = BeautifulSoup(page_to_scrape.text,'html.parser')
#find all the items in the page with a class attr of 'text'
#store the lists as a variable
quotes = soup.findAll('span', attrs={'class':'text'})

#find all the items with a class attr of "author"
#store the lists as a var
authors = soup.findAll('small',attrs={'class':'author'})

##find all the items with a class attr of "tag"
#store the lists as a var
tags = soup.findAll('span', attrs={'class':'tag-item'})

#loop through both lists using the zip function
#print and format the results
for quote, author, tag in zip(quotes,authors,tags):
  print(quote.text + "-" + author.text + "-" + tag.text)
  
  #write each item as a new row in the csv
  writer.writerow([quote.text,author.text,tag.text])

#close the csv file
file.close()

