#!/usr/bin/python3
"""Querry the Reddit API and returns the number of subscribers"""


import requests


def number_of_subscribers(subreddit):
    """ Query starts """
    headers = {'User-Agent': 'Agent1'}
    url = f'https://www.reddit.com/r/{subreddit}/about.json'

    try:
        response = requests.get(url, headers=headers, allow_redirects=False)
        response.raise_for_status()
        data = response.json()
        return data['data']['subscribers']

    except requests.exceptions.HTTPError:
        return 0
