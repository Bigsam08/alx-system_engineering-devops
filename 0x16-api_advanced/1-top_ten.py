#!/usr/bin/python3
""" QUERY TOP 10 """


import requests
import sys


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts
    listed for a given subreddit.
    """

    headers = {'User-Agent': 'MyRedditagent/0.1'}
    url = f'https://www.reddit.com/r/{subreddit}/hot.json?limit=10'

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        display = data['data']['children']

        for i in range(min(10, len(display))):
            print(displY[i]['data']['title'])

        except requests.exceptions.HTTPError:
            print("None")
        except KeyError:
            print("None")


if __name__ == '__main__':
    top_ten(sys.argv[1])
