import os
from urllib.request import urlopen

def download_url(url):
    """Saves target URL to disk"""
    filename = url.split("/")[-1]
    if not os.path.isfile(filename):
        print("Writing pdf file - " + filename)
        with open(filename, "wb") as pdf_file:
            try:
                pdf_file.write(urlopen(url).read())
            except:
                print("Couldn't download or write pdf")
