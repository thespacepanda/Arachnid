class LinkSource(object):
    """LinkSource produces a flat list of URLs aggregated from various LinkProducers"""

    def __init__(self, linkProducers=[]):
        """LinkSource is initialized with a list of LinkProducers"""
        self._producers = linkProducers
        self._consumed_links = set()

    def tap(self):
        """Returns a generator which returns links from the producers"""
        for producer in self._producers:
            for link in producer.get_links():
                if link not in self._consumed_links:
                    self._consumed_links.add(link)
                    yield link
