import DownloadManager
import LinkManager
import TargetFilter
import time

class Arachnid(object):
    """Arachnid manages the life cycle of the other objects"""

    def __init__(self):
        self._link_manager = LinkManager.LinkManager()

    def run_downloader(self):
        print("running downloader...")
        while True:
            for url in self._link_manager.get_links():
                try:
                    print("Current URL: {}".format(url))
                    if TargetFilter.target_filter(url):
                        print("{} matches target filter".format(url))
                        DownloadManager.download_url(url)
                except:
                    print("Failed on the current url for some reason")

if __name__ == "__main__":
    arachnid = Arachnid()
    arachnid.run_downloader()
