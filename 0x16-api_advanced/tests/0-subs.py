#!/usr/bin/python3
"""returns number of users in a subreddit"""

import requests


def number_of_subscribers(subreddit):
    """
    get number of subscribers
    if subreddit is not valid return 0

    Args::
        subreddit
    """
    reddit_url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
            "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
            }

    response = requests.get(reddit_url, headers=headers, allow_redirects=False)

    if response.status_code == 404:
        return 0
    results = response.json().get("data")
    return results.get("subscribers")
