import praw
import config
import LinkProducer

class RedditBot(LinkProducer.LinkProducer):
    """RedditBot is a LinkProducer which crawls the subreddits specified in the config"""

    def __init__(self):
        """RedditBot pulls in the subreddits from the config file and creates a praw.Reddit instance"""
        self.user_agent = "Arachnid (by /u/briticus557)"
        self.reddit = praw.Reddit(user_agent=self.user_agent)
        self.subreddits = []
        for subreddit in config.subreddits:
            self.subreddits.append(self.reddit.get_subreddit(subreddit))

    def get_links(self):
        """Returns a list of URLs from the configured subreddits"""
        links = []
        for subreddit in self.subreddits:
            for post in subreddit.get_hot():
                links.append(post.url)
        return links
