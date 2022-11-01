#!/usr/bin/python3
"""prints the titles of the first 10 hot posts"""
import requests


def top_ten(subreddit):
    """
    gets titles of the top ten hot posts for a given subreddit
    if not valid subreddit return None

    args::
        subreddit: specified subreddit
    """

    reddit_url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
            "User-Agent": "linux:0x16.api.advanced:v1.0.0 (by /u/bdov_)"
            }

    response = requests.get(reddit_url, headers=headers, allow_redirects=False)
    if response.status_code == 404:
        return None
    results = response.json().get("data")
    for child in results.get("children"):
        topics = child.get("data").get("title")
        print(topics)
    #[print(c.get("data").get("title")) for c in results.get("children")]
