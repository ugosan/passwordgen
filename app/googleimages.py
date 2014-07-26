#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
import time
from urllib import FancyURLopener
import urllib2
import simplejson


imagePath = '/Users/ugosan/temp/xkcd/'
#imagePath = '/home/sablot/sablot/searchedImages/'

# Start FancyURLopener with defined version 
class MyOpener(FancyURLopener): 
    version = 'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11'


class GoogleImagesSearch:

    def query(self, searchTerm):
        
        # Replace spaces ' ' in search term for '%20' in order to comply with request
        searchTerm = str(searchTerm).replace(' ','%20')
        
        myopener = MyOpener()
        
        images = []
        
        #pages of results
        for i in range(0,1):
            
            # Notice that the start changes for each iteration in order to request a new set of images for each loop
            url = ('https://ajax.googleapis.com/ajax/services/search/images?v=1.0&q='+searchTerm+'&start='+str(i*4)+'&userip=MyIP')
            
            request = urllib2.Request(url, None, {'Referer': 'testing'})
            response = urllib2.urlopen(request)

            # Get results using JSON
            results = simplejson.load(response)
            data = results['responseData']
            dataInfo = data['results']
            
            
            # Iterate for each result and get unescaped url
            for myUrl in dataInfo:
                

                images.append(myUrl['unescapedUrl'])
        
        #print images
        return images
    
    
if __name__ == "__main__":
    gi = GoogleImagesSearch()
    gi.query(['%s'%(sys.argv[1])])

