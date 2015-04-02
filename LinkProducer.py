from abc import ABCMeta, abstractmethod

class LinkProducer(object):
    """LinkProducer is an interface for classes which produce URLs"""
    __metaclass__ = ABCMeta

    @abstractmethod
    def get_links(self):
        pass
