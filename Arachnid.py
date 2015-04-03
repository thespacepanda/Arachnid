import LinkManager

class Arachnid(object):
    """Arachnid manages the life cycle of the other objects"""

    def __init__(self):
        self._link_manager = LinkManager.LinkManager()

    def test(self):
        set_a = self._link_manager.get_links()
        set_b = self._link_manager.get_links()
        print(len(set_a))
        print(len(set_b))

if __name__ == "__main__":
    arachnid = Arachnid()
    arachnid.test()
