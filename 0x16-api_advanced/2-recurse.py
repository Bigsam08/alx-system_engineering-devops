#!/usr/bin/python3
"""
    A recursive function that queries the Reddit
    API and returns titles of
    all hot articles.
"""
import requests


def recurse(subreddit, hot_list=[], after="", count=0):
    """ code """
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {
        "User-Agent": "User-Agent"
    }
    params = {
        "after": after,
        "count": count,
        "limit": 100
    }
    response = requests.get(url, headers=headers, params=params,
                            allow_redirects=False)
    if response.status_code == 404:
        return None

    alist = response.json().get("data")
    after = alist.get("after")
    count += alist.get("dist")
    for i in alist.get("children"):
        hot_list.append(i.get("data").get("title"))

    if after is not None:
        return recurse(subreddit, hot_list, after, count)
    return hot_list
