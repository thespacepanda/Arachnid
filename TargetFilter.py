import config

def target_filter(url_set):
    """Removes all URLs from the set which are not the target filetype"""
    filetype = "." + config.target_filetype

    def filetype_predicate(url):
        """Matches if URL is a link to the given filetype"""
        return filetype in url

    return filter(filetype_predicate, url_set)
