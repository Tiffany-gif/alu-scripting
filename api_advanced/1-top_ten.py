#!/usr/bin/python3
"""Script that fetches 10 hot posts for a given subreddit."""
import requests


def top_ten(subreddit):
    """Print the titles of the first 10 hot posts of a subreddit.
    Print None if subreddit is invalid or has no posts.
    """

    headers = {'User-Agent': 'python:subreddit.hot:v1.0 (by /u/fakeuser123)'}
    subreddit_url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)

    try:
        response = requests.get(subreddit_url, headers=headers, allow_redirects=False)

        if response.status_code != 200:
            print(None)
            return

        posts = response.json().get('data', {}).get('children', [])

        if not posts:
            print(None)
            return

        for post in posts:
            print(post.get('data', {}).get('title'))

    except Exception:
        print(None)

