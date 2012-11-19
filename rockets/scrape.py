import os.path, urllib  
import exceptions, urllib2, re
from BeautifulSoup import BeautifulStoneSoup
import sys

# url = 'http://grin.hq.nasa.gov/BROWSE/rocket_launch.html' # all the things
url = 'http://grin.hq.nasa.gov/BROWSE/rocket_launch_7.html' # just one page

base_url = 'http://grin.hq.nasa.gov'

try:
    page = urllib2.urlopen(url).read()   
except urllib2.HTTPError:
    raise Exception("Http 404 - invalid start url: " + url)

soup = BeautifulStoneSoup(page) 
all_links = soup.findAll('a')   





images = {}
for link in all_links:
	if len(images) == 0:
		# first look for the image link
		if link.find('img'):
			images['title'] = str(link.find('img')['alt'])
			images['large_image'] = base_url + link['href']
			images['thumbnail'] = base_url + str(link.find('img')['src'])

	if len(images) == 3:
		if str(link.contents[0]) == 'More information':
			# we have the image link, look for the more_info link
			images['more_info_link'] = base_url + link['href']
			print 'image array:'
			print images
			images = {}
			print '------------------------------'

# scraperwiki.sqlite.save(unique_keys=['Time'], data=data)

