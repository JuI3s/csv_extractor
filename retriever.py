from bs4 import BeautifulSoup
import urllib2
import requests
from urlparse import urljoin
import os
import csv
 
class DataRetriever:

	def __init__(self, base_url): 
		self.base_url = base_url

	#Return all the urls containing csv files contained in data_url
	def get_csv_links(self, data_url = ""):
		if data_url == "":
			data_url = self.base_url
		r = requests.get(data_url)
		data = r.text
		soup = BeautifulSoup(data, "html.parser") 
		csv_links = [];

		for link in soup.find_all('a'):
			url = link.get('href')
			if str(url).endswith('.csv', (len(str(url)) - 4)):
				url = urljoin(data_url, url)
				csv_links.append(str(url))

		return csv_links

	#Download csv data file from a url to directory
	@staticmethod 
	def download_csv_file(url):
		#Create data directory if not already existent
		dir_name = 'data_files'
		if not os.path.exists("./" + dir_name):
			os.mkdir(dir_name)

		#get the file name
		filename = url.rsplit('/', 1)[-1]
		#writing files to dir
		filename = dir_name + '/' + filename
		response = urllib2.urlopen(url)
		cr = csv.reader(response)

		with open(filename, 'wb') as csvfile: 
			cw = csv.writer(csvfile)
			for row in cr: 
				cw.writerow(row)

		print("Finished writing " + filename + " to directory: " + dir_name)

	#Return all field attributes from a row that does not contain empy fields
	@staticmethod
	def extract_fields(row, *kargs): 
		records = dict()
		empty = False

		for each in kargs:
			records[each] = row[each]
			if row[each] == "": 
				return None
		return records
