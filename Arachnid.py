import DownloadManager
import LinkManager
import TargetFilter

def main():
    while True:
        for url in LinkManager.LinkManager().get_links():
            try:
                if TargetFilter.target_filter(url):
                    DownloadManager.download_url(url)
            except:
                print("failed on current url")

if __name__ == "__main__":
    main()
