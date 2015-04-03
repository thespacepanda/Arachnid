import DownloadManager
import LinkManager
import TargetFilter

class Arachnid(object):
    """Arachnid manages the life cycle of the other objects"""

    def __init__(self):
        self._link_manager = LinkManager.LinkManager()

    def run_downloader(self):
       url_set = self._link_manager.get_links()
       pdf_set = TargetFilter.target_filter(url_set)
       DownloadManager.download_urls(pdf_set)

if __name__ == "__main__":
    arachnid = Arachnid()
    arachnid.run_downloader()
