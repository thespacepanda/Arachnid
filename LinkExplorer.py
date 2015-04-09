import config
import functools
import httplib2
import sys
import util
from bs4 import BeautifulSoup, SoupStrainer
from multiprocessing import Pool

class LinkExplorer(object):
    """LinkExplorer crawls over URLs, aggregating links to a specified depth"""

    def __init__(self, linkSource):
        """LinkExplorer is initialized with a LinkSource"""
        self._source = linkSource
        self._visited = set()
        self._http = httplib2.Http()

    def explore(self):
        """Lazily returns sets of urls crawled from the LinkSource"""

        def delve(current_url, current_depth):
            """Returns all links referenced by the url until current_depth is 0"""
            self._visited.add(current_url)
            url_links = set([current_url])
            try:
                status, response = self._http.request(current_url)
            except:
                print(sys.exc_info()[:2])
                return
            for link in BeautifulSoup(response,
                                      parse_only=SoupStrainer("a", href=True)
                                      ).find_all("a"):
                if not self._source.in_producer_domain(link["href"]):
                    if link["href"] not in self._visited:
                        self._visited.add(link["href"])
                        url_links.add(link["href"])
            if current_depth is 0:
                yield from url_links
            else:
                with Pool(len(url_links)) as p:
                    delve_to = util.flip(delve)
                    delve_to_depth = functools.partial(delve_to, current_depth-1)
                    yield from p.map(delve_to_depth, url_links)
                yield from url_links

        depth = config.page_depth
        for url in self._source.tap():
            for link in delve(url, depth):
                yield link
