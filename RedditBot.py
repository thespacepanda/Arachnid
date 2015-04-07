import praw
import config
import LinkProducer

class RedditBot(LinkProducer.LinkProducer):
    """RedditBot is a LinkProducer which crawls subreddits specified in the config"""

    def __init__(self):
        self.user_agent = "Arachnid (by /u/briticus557)"
        self.reddit = praw.Reddit(user_agent=self.user_agent)
        self.subreddits = []
        for subreddit in config.subreddits:
            self.subreddits.append(self.reddit.get_subreddit(subreddit))
        super().__init__("reddit.com")

    def get_links(self):
        """Lazily returns iterable of URLs from configured subreddits"""
        for subreddit in self.subreddits:
            for post in subreddit.get_hot():
                yield post.url
