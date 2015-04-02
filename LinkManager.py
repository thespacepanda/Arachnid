import LinkExplorer
import LinkSource
import RedditBot

class LinkManager(object):
    """LinkManager handles the creation and polling of the LinkExplorer"""

    def __init__(self):
        reddit = RedditBot.RedditBot()
        source = LinkSource.LinkSource([reddit])
        self._explorer = LinkExplorer.LinkExplorer(source)

    def link_stream(self):
        """Generates a stream of semi-unique URLs"""
        for url_set in self._explorer.explore():
            for url in url_set:
                yield url
