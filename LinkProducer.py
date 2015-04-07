from abc import ABCMeta, abstractmethod

class LinkProducer(object):
    """LinkProducer is an interface for classes which produce URLs"""
    __metaclass__ = ABCMeta

    def __init__(self, domain):
        """Associates this producer with the domain"""
        self.domain = domain

    @abstractmethod
    def get_links(self):
        """Lazily returns iterable of URLs"""
        pass
