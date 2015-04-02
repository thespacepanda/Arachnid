import config
import httplib2
from BeautifulSoup import BeautifulSoup, SoupStrainer

class LinkExplorer(object):
    """LinkExplorer crawls over URLs, aggregating links to a specified depth"""

    def __init__(self, linkSource):
        """LinkExplorer is initialized with a LinkSource"""
        self._source = linkSource
        self._visited_links = set()

