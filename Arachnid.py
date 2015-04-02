import LinkExplorer
import LinkSource
import RedditBot

class Arachnid(object):
    """Arachnid manages the life cycle of the other objects"""

    def __init__(self):
        """Constructs necessary owned objects"""
        reddit = RedditBot.RedditBot()
        source = LinkSource.LinkSource([reddit])
        self.explorer = LinkExplorer.LinkExplorer(source)

    def test(self):
        for url_set in self.explorer.explore():
            for url in url_set:
                print(url)

if __name__ == "__main__":
    arachnid = Arachnid()
    arachnid.test()
