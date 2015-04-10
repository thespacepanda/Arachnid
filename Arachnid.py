import functools
import httplib2
import os
import praw
from bs4 import BeautifulSoup, SoupStrainer
from multiprocessing.dummy import Pool
from urllib.request import urlopen, URLError
from util import coroutine, sending, printing

http = httplib2.Http()

def fetching(sources, target):
    for source in sources:
        sending(target, source)

def reddit(subreddits):
    user_agent = "Arachnid (by /u/briticus557)"
    r = praw.Reddit(user_agent=user_agent)
    subs = (r.get_subreddit(sub) for sub in subreddits)
    for sub in subs:
        for post in sub.get_hot():
            yield post.url

@coroutine
def crawling(strategy, target):
    while True:
        item = (yield)
        sending(target, strategy(item))

def recursively(until, url):
    links = set([url])
    try:
        status, response = http.request(url)
    except httplib2.HttpLib2Error:
        printing("Error requesting {}".format(url))
        return
    except KeyError:
        printing("Tried to access non-http resource")
    for link in BeautifulSoup(response,
                              parse_only=SoupStrainer("a",
                                                      href=True)
                             ).find_all("a"):
        links.add(link["href"])
    if until is 0:
        for link in links:
            yield link
    else:
        with Pool(len(links)) as pool:
            delve = functools.partial(recursively, until-1)
            for crawler in pool.map(delve, links):
                for link in crawler:
                    yield link
        for link in links:
            yield link

@coroutine
def filtering(predicate, target):
    while True:
        crawled = (yield)
        printing(crawled)
        if predicate(crawled):
            target.send(crawled)

@coroutine
def downloading():
    while True:
        url = (yield)
        filename = url.split("/")[-1]
        if not os.path.isfile(filename):
            try:
                data = urlopen(url).read()
            except URLError:
                printing("Couldn't download {}".format(url))
                continue
            with open(filename, "wb") as maybe:
                maybe.write(data)

if __name__ == "__main__":
    producers = [reddit(["haskell", "python", "learnprogramming"])]
    filetype = ".pdf"
    matches = lambda url: filetype in url.lower()
    delve = functools.partial(recursively, 3)
    fetching(producers,
             crawling(delve,
             filtering(matches,
             downloading())))
