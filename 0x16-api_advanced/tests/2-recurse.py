#!/usr/bin/python3
"""
returns the titles of all hot articles for a subreddit
"""
import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """
    returns a list of hot titles
    args::
        subreddit: specified subreddit
        hot_list(list): list of all the hot tittles
        count(int): keeps count of number of recurses
    """

    reddit_url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
            "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
            }

    params = {
        "after": after,
        "count": count,
        "limit": 100
    }
    response = requests.get(reddit_url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 404:
        return None
    results = response.json().get("data")
    after = results.get("after")
    count += results.get("dist")
    for c in results.get("children"):
        hot_list.append(c.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list
