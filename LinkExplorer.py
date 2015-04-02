import config
import httplib2
from bs4 import BeautifulSoup, SoupStrainer

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
            print("delve called on url: {}, depth: {}".format(current_url, current_depth))
            self._visited.add(current_url)
            url_links = set([current_url])
            try:
                status, response = self._http.request(current_url)
            except httplib2.RelativeURIError:
                return url_links
            for link in BeautifulSoup(response,
                                      parse_only=SoupStrainer("a", href=True)
                                      ).find_all("a"):
                if link["href"] not in self._visited:
                    self._visited.add(link["href"])
                    url_links.add(link["href"])
            if current_depth is 0:
                return url_links
            else:
                children_urls = set()
                for url in url_links:
                    children_urls = children_urls.union(delve(url, current_depth-1))
                return url_links.union(children_urls)

        depth = config.page_depth
        for url in self._source.tap():
            yield delve(url, depth)
