#!/usr/bin/python3
"""Querry the Reddit API and returns the number of subscribers"""
import requests


def number_of_subscribers(subreddit):
    response = requests.get("https://www.reddit.com/r/{}/about.json"
                            .format(subreddit),
                            headers={"User-Agent": "UserAgent"},
                            allow_redirects=False)
    if response.status_code == 404:
        return 0

    return response.json().get("data").get("subscribers")
