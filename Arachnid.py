import LinkSource
import RedditBot

class Arachnid(object):
    """Arachnid manages the life cycle of the other objects"""

    def __init__(self):
        """Constructs necessary owned objects"""
        reddit = RedditBot.RedditBot()
        self.source = LinkSource.LinkSource([reddit])

    def test(self):
        for link in self.source.tap():
            print(link)


if __name__ == "__main__":
    arachnid = Arachnid()
    arachnid.test()
