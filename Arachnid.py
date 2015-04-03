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
            print("getting links...")
            url_set = self._link_manager.get_links()
            print("got links")
            print("filtering for pdfs...")
            pdf_set = TargetFilter.target_filter(url_set)
            print("just pdfs now")
            print("downloading pdfs...")
            DownloadManager.download_urls(pdf_set)
            print("sleeping 30 seconds")
            time.sleep(30)
            print("done sleeping!")

if __name__ == "__main__":
    arachnid = Arachnid()
    arachnid.run_downloader()
