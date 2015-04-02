import LinkManager

class Arachnid(object):
    """Arachnid manages the life cycle of the other objects"""

    def __init__(self):
        self._link_manager = LinkManager.LinkManager()

    def test(self):
        for link in self._link_manager.link_stream():
            print(link)

if __name__ == "__main__":
    arachnid = Arachnid()
    arachnid.test()
