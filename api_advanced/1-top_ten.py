#!/usr/bin/python3
"""Exporting csv files (but actually just prints top 10 hot posts). """
import requests


def top_ten(subreddit):
    """Read Reddit API and print top 10 hot posts titles for a subreddit."""
    headers = {'User-Agent': 'python:holberton.topten:v1.0 (by /u/ledbag123)'}
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)

    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        try:
            posts = response.json()['data']['children']
            for post in posts[:10]:
                print(post['data']['title'])
        except Exception:
            print(None)
    else:
        print(None)
