#!/usr/bin/python3
"""
    Queries the Reddit API and returns the top 10 hot posts
    of the subreddit
"""
import requests


def top_ten(subreddit):
    """top 10"""
    response = requests.get("https://www.reddit.com/r/{}/hot.json?limit=10"
                            .format(subreddit),
                            headers={"User-Agent": "My-User-Agent"},
                            allow_redirects=False)
    if sub_info.status_code == 400:
        print('None')
    else:
        [print(child.get("data").get("title"))
         for child in sub_info.json().get("data").get("children")]
