import LinkManager
import TargetFilter

class Arachnid(object):
    """Arachnid manages the life cycle of the other objects"""

    def __init__(self):
        self._link_manager = LinkManager.LinkManager()
        self._target_filter = TargetFilter.target_filter

    def test(self):
       url_set = self._link_manager.get_links()
       for pdf in self._target_filter(url_set):
           print(pdf)

if __name__ == "__main__":
    arachnid = Arachnid()
    arachnid.test()
