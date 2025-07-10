#!/usr/bin/python3
"""DOCS"""
import requests


def top_ten(subreddit):
    """Docs"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {'User-agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        data = response.json().get('data', {}.get('children'[])
        if not data:
            print(None)
    else:
        for post in data:
            print(post.get('data'), {}).get('title'))
    else:
        print(None)
print("OK", end="")
