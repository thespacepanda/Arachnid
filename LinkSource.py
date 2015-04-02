class LinkSource(object):
    """LinkSource produces a flat list of URLs aggregated from various LinkProducers"""

    def __init__(self, LinkProducers=[]):
        """LinkSource is initialized with a list of LinkProducers"""
        self.producers = LinkProducers
        self._consumed_links = set()

    def tap(self):
        """Returns a generator which returns links from the producers"""
        for producer in self.producers:
            for link in producer.get_links():
                if not link in self._consumed_links:
                    self._consumed_links.add(link)
                    yield link
