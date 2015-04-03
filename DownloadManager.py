import os
import urllib2

def download_urls(url_set):
    """Saves target URLs to disk"""
    for url in url_set:
        filename = url.split("/")[-1]
        if not os.path.isfile(filename):
            print("Writing pdf file - " + filename)
            with open(filename, "wb") as pdf_file:
                pdf_file.write(urllib2.urlopen(url).read())
