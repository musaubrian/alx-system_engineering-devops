#!/usr/bin/python3
"""
parses the title of all hot articles, and prints a sorted count list
"""


import re
import requests


def add_title(dictionary, hot_posts):
    """
    Adds item into a list
    args::
        dictionary: dictionary to add lists to
        hot_posts: reddit's hto posts
    """
    hot_posts.pop(0)
    add_title(dictionary, hot_posts)
    if len(hot_posts) == 0:
        return

    title = hot_posts[0]['data']['title'].split()
    for word in title:
        for key in dictionary.keys():
            c = re.compile("^{}$".format(key), re.I)
            if c.findall(word):
                dictionary[key] += 1
    hot_posts.pop(0)
    add_title(dictionary, hot_posts)


def recurse(subreddit, dictionary, after=None):
    """
    Queries to Reddit API
    Args::
        subreddit: specified subreddit
        dictionary: where topics are *stored
    """
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }

    params = {
        'after': after
    }

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    res = requests.get(url,
                      headers=headers,
                      params=params,
                      allow_redirects=False)

    if res.status_code != 200:
        return None

    dic = res.json()
    hot_posts = dic['data']['children']
    add_title(dictionary, hot_posts)
    after = dic['data']['after']
    if not after:
        return
    recurse(subreddit, dictionary, after=after)


def count_words(subreddit, word_list):
    """ 
    Init function
    args::
        subreddit: specified subreddit
        word_list:
    """
    dictionary = {}

    for word in word_list:
        dictionary[word] = 0

    recurse(subreddit, dictionary)

    l = sorted(dictionary.items(), key=lambda kv: kv[1])
    l.reverse()

    if len(l) != 0:
        for item in l:
            if item[1] != 0:
                print("{}: {}".format(item[0], item[1]))
    else:
        print("")
