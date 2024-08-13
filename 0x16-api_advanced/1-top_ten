#!/usr/bin/python3
"""
    Queries the Reddit API and returns the top 10 hot posts
    of the subreddit
"""
import requests


def top_ten(subreddit):
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "User-Agent)"
    }
    params = {
        "limit": 10
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 404:
        print("None")
        return
    sub_list = response.json().get("data")
    [print(i.get("data").get("title")) for i in sub_list.get("children")]
