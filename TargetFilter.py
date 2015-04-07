import config

def target_filter(url):
    """Matches if URL is a link to the configured filetype"""
    filetype = "." + config.target_filetype
    return filetype in url.lower()
